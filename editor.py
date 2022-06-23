import subprocess
from math import ceil

from PIL import Image, ImageQt
import numpy as np
import ffmpeg

from PySide6.QtCore import Qt, QThread
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QDialog

import functools
import functions_ui

from dialog import Ui_Dialog


def probe(metadata, keys):
    def get_nested_item(d, k, type=str, sep='.'):
        _k = k.split(sep)
        item = d.get(_k[0], None)
        if isinstance(item, dict):
            item = get_nested_item(item, sep.join(_k[1:]), type, sep)
        try:
            item = type(item)
        except Exception:
            item = item
        return item

    video_streams = [s for s in metadata['streams'] if s['codec_type'] == 'video']
    audio_streams = [s for s in metadata['streams'] if s['codec_type'] == 'audio']

    _metadata = []
    for (k, t) in keys:
        if k.startswith('format'):
            m = get_nested_item(metadata, k, t)
        else:
            _k = '.'.join(k.split('.')[1:])
            streams = video_streams if k.startswith('video') else audio_streams
            for s in streams:
                m = get_nested_item(s, _k, t)
                if m is not None:
                    break
        _metadata.append(m)
    return _metadata


METADATA_KEY_MAP = {
    'format': ('format.format_name', str),
    'duration': ('format.duration', float),
    'size': ('format.size', int),

    'video_codec': ('video.codec_name', str),
    'width': ('video.width', int),
    'height': ('video.height', int),
    'rotate': ('video.tags.rotate', int),
    'framecount': ('video.nb_read_frames', int),
    'framerate': ('video.avg_frame_rate', float),

    'audio_codec': ('audio.codec_name', str),
}
from typing import NamedTuple
from collections import OrderedDict


class Editor:
    def __init__(self):
        self._video = None
        self.metadata = None
        self.thumbnail = None
        self.thumbnail_transformed = None
        self.transforms = OrderedDict()

    def reset_video(self):
        self._video = None
        self.metadata = None
        self.thumbnail = None

    def reset_transforms(self):
        self.transforms = OrderedDict()

    @property
    def video(self):
        return self._video

    @video.setter
    def video(self, path):
        self.reset_video()
        self._video = path

    def parse_metadata(self):
        metadata = ffmpeg.probe(self.video, print_format='json', show_format=None, count_frames=None)

        metadata = probe(metadata, METADATA_KEY_MAP.values())
        self.metadata = dict(zip(METADATA_KEY_MAP.keys(), metadata))

    def extract_thumbnail(self):
        if not self.video:
            return False

        if not self.metadata:
            self.parse_metadata()

        cmd = (ffmpeg.input(self.video, vsync=2)
               .filter('thumbnail', n=self.metadata['framecount'])
               .output('pipe:1', vframes=1, vcodec='rawvideo', format='image2pipe')
               .global_args('-loglevel', 'error')
               .global_args('-hide_banner')
               )
        w, h = self.metadata['width'], self.metadata['height']
        buf_size = w * h * 3
        proc = subprocess.Popen(cmd.compile(), stdout=subprocess.PIPE, bufsize=buf_size)

        stdout = proc.stdout.read(w * h * 3)
        proc.stdout.flush()
        image = Image.frombuffer('RGB', (w, h), stdout, "raw", 'RGB', 0, 1)

        return image

    @classmethod
    def extract_thumbnail_(cls, path):
        metadata = cls.parse_metadata_(path)
        cmd = (ffmpeg.input(path, vsync=2)
               .filter('thumbnail', n=metadata['framecount'])
               .output('pipe:1', vframes=1, vcodec='rawvideo', format='image2pipe')
               .global_args('-loglevel', 'error')
               .global_args('-hide_banner')
               )
        w, h = metadata['width'], metadata['height']
        buf_size = w * h * 3
        proc = subprocess.Popen(cmd.compile(), stdout=subprocess.PIPE, bufsize=buf_size)
        stdout = proc.stdout.read(w * h * 3)
        proc.stdout.flush()
        image = Image.frombuffer('RGB', (w, h), stdout, "raw", 'RGB', 0, 1)
        return image

    @classmethod
    def parse_metadata_(cls, path):
        metadata = ffmpeg.probe(path, print_format='json', show_format=None, count_frames=None)

        metadata = probe(metadata, METADATA_KEY_MAP.values())
        metadata = dict(zip(METADATA_KEY_MAP.keys(), metadata))
        return metadata

    def append_transform(self, key, value):
        self.transforms[key] = value
        self.transforms.move_to_end(key, last=True)

    def remove_transform(self, key):
        if self.transforms.get(key):
            self.transforms.pop(key)

    def build_transform_streams(self, input_stream, input_w, input_h):
        stream = input_stream
        tw, th = input_w, input_h
        for key, param in self.transforms.items():
            if key == 'brightness':
                stream = stream.filter('eq', brightness=param['value'] * 0.01)
            elif key == 'contrast':
                stream = stream.filter('eq', contrast=param['value'] * 0.01 + 1)
            elif key == 'rotate':
                if param['value'] == 90:
                    stream = stream.filter('transpose', 1)
                    tw, th = th, tw
                elif param['value'] == 180:
                    stream = stream.filter('transpose', 2).filter('transpose', 2)
                elif param['value'] == 270:
                    stream = stream.filter('transpose', 2)
                    tw, th = th, tw
            elif key == 'flip':
                if param['value'] == 'horizontal':
                    stream = stream.hflip()
                elif param['value'] == 'vertical':
                    stream = stream.vflip()
                elif param['value'] == 'all':
                    stream = stream.hflip().vflip()
            elif key == 'fps':
                stream = stream.filter('fps', fps=param['value'], round='up')
            elif key == 'grayscale' and param['value']:
                stream = stream.filter('hue', s=0)
            elif key == 'crop':
                r = param['value'] * 0.01
                x, y = int(tw * r * 0.5), int(th * r * 0.5)
                tw = ceil((tw - 2 * x) * 0.5) * 2
                th = ceil((th - 2 * y) * 0.5) * 2
                stream = stream.filter('crop', x=x, y=y, w=tw, h=th)
            elif key == 'border':
                bw, bh = tw * param['w'] * 0.005, th * param['h'] * 0.005
                tw = ceil((tw + 2 * bw) * 0.5) * 2
                th = ceil((th + 2 * bh) * 0.5) * 2
                stream = stream.filter('pad', x=bw, y=bh, w=tw, h=th, color='black')

            elif key == 'resolution':
                if param['selector'] == 'preset':
                    if param['preset'] == 'CIF':
                        tw, th = 352, 240
                    elif param['preset'] == 'QCIF':
                        tw, th = 176, 144
                    elif param['preset'] == 'SD':
                        tw, th = 320, 240
                elif param['selector'] == 'ratio':
                    r = (param['ratio'] + 100) * 0.01
                    tw, th = ceil(tw * r * 0.5) * 2, ceil(th * r * 0.5) * 2

                stream = stream.filter('scale', w=tw, h=th)
            elif key == 'pip':
                px, py = tw * param['size'] * 0.005, th * param['size'] * 0.005
                tw = ceil((tw + 2 * px) * 0.5) * 2
                th = ceil((th + 2 * py) * 0.5) * 2
                background = ffmpeg.input(param['background']).filter('scale', w=tw, h=th)
                stream = background.overlay(stream, x=px, y=py)
            elif key == 'logo':
                lw, lh = int(tw * param['size'] * 0.01), int(th * param['size'] * 0.01)
                lx = int((tw - lw) * param['x'] * 0.01)
                ly = int((th - lh) * param['y'] * 0.01)

                logo = ffmpeg.input(param['logo']).filter('scale', w=lw, h=lh)
                stream = stream.overlay(logo, x=lx, y=ly)
            elif key == 'caption':
                fx = int(param['x'] * tw * 0.01)
                fy = int(param['y'] * th * 0.01)

                stream = stream.drawtext(text=param['text'], fontcolor=param['color'], fontsize=param['size'],
                                         x=fx, y=fy, font=param['font'])
        return stream, tw, th

    def get_thumbnail(self, viewer_size):
        if not self.video:
            return False

        if not len(self.transforms):
            return self.resize_thumbnail(self.thumbnail, viewer_size)

        origin = self.thumbnail
        w, h = origin.size

        stream = ffmpeg.input('pipe:0', format='rawvideo', pix_fmt='rgb24', s='{}x{}'.format(w, h))
        stream, target_w, target_h = self.build_transform_streams(stream, w, h)
        stream = stream.output('pipe:1', vframes=1, format='rawvideo', pix_fmt='rgb24').global_args('-hide_banner')

        proc = subprocess.Popen(stream.compile(), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        proc.stdout.flush()
        (stdout, stderr) = proc.communicate(input=np.array(origin).tobytes())
        target = Image.fromarray(np.frombuffer(stdout, np.uint8).reshape([target_h, target_w, 3]))
        return self.resize_thumbnail(target, viewer_size)

    def get_video_transform_command(self, target_path):

        input_stream = ffmpeg.input(self.video)
        input_w, input_h = self.metadata['width'], self.metadata['height']
        stream, *_ = self.build_transform_streams(input_stream, input_w, input_h)

        stream = stream.output(target_path, vcodec='libx264', acodec='aac') \
            .global_args('-hide_banner') \
            .global_args('-nostats') \
            .global_args('-progress', 'pipe:1') \
            .overwrite_output()

        return stream.compile()

    @classmethod
    def resize_thumbnail(cls, image, target):
        w, h = cls.get_maximum_size(image.width, image.height, target[0], target[1])

        return image.resize((w, h))

    @classmethod
    def to_QtPixmap(cls, image):
        return ImageQt.toqpixmap(image)

    @classmethod
    def get_maximum_size(cls, w, h, max_w, max_h):
        r1, r2 = (max_w / w, max_h / h)
        nw, nh = (int(w * r1), int(h * r1)) if r1 < r2 else (int(w * r2), int(h * r2))

        return nw, nh


class VideoTransformDialog(QDialog):
    def __init__(self, command, max_len, log=None, parent=None):
        super(VideoTransformDialog, self).__init__(parent=parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.progressBar.setMinimum(1)
        self.ui.progressBar.setMaximum(max_len)
        self.ui.close_btn.setEnabled(False)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.close_btn.clicked.connect(lambda: self.close())
        self.ui.dialog_header.mouseMoveEvent = functools.partial(functions_ui.moveWindow, window=self)

        self.progress = None
        self.command = command
        self.log = log

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()  # monitor pos
        if event.buttons() == Qt.LeftButton:
            print(f'Mouse L_BTN_DOWN: {self.dragPos}')
        if event.buttons() == Qt.RightButton:
            print(f'Mouse R_BTN_DOWN: {self.dragPos}')
        if event.buttons() == Qt.MiddleButton:
            print(f'Mouse M_BTN_DOWN: {self.dragPos}')

    def showModal(self):
        self.ui.progressBar.setValue(self.ui.progressBar.minimum())

        self.vt_thread = VideoTransformThread(self.ui, self.command, self.receive_outputs, self.log)
        self.ui.command_te.setPlainText(' '.join(self.command))
        self.ui.log_label.setText(f'Log: {self.log}')

        self.vt_thread.start()
        self.exec()
        self.vt_thread.stop()

    def receive_outputs(self, status, line):
        try:
            if status:
                if isinstance(line, bytes):
                    line = line.decode(encoding='utf8').strip()

                if line.startswith('frame='):
                    frame = int(line.split('frame=')[1])
                    self.ui.progressBar.setValue(frame)
                if line.startswith('progress='):
                    self.progress = line.split('progress=')[1]
            else:
                # Done or err

                self.ui.close_btn.setEnabled(True)
                if self.progress != 'end':
                    print('error')
                    self.vt_thread.stop()
                else:
                    self.ui.progressBar.setValue(self.ui.progressBar.maximum())

        except Exception as e:
            print(e)
            self.vt_thread.stop()


class VideoTransformThread(QThread):
    def __init__(self, ui, command, receiver, log=None):
        super(VideoTransformThread, self).__init__()
        self.ui = ui
        self.command = command
        self.receiver = receiver
        self.log = log

    def send_stdout(self, pipe):
        try:
            with pipe:
                for line in iter(pipe.readline, b''):
                    self.receiver(True, line)
        finally:
            self.receiver(False, None)

    def run(self):
        stderr = open(self.log, 'w') if self.log else subprocess.PIPE

        proc = subprocess.Popen(self.command, stdout=subprocess.PIPE, stderr=stderr)
        self.send_stdout(proc.stdout)
        if self.log:
            stderr.write(' '.join(self.command))
            stderr.close()

    def stop(self):
        self.quit()
        self.wait(1000)
