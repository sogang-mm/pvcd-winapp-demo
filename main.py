import os.path
import sys
import platform
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QColor,
                           QFont, QFontInfo, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform, QIntValidator, QValidator)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
                               QGroupBox, QHBoxLayout, QLabel, QLineEdit, QFileDialog,
                               QMainWindow, QPushButton, QRadioButton, QSizePolicy,
                               QSlider, QStackedWidget, QToolButton, QVBoxLayout,
                               QWidget, QFontDialog, QColorDialog, QErrorMessage, QTableWidgetItem, QHeaderView)
from pathlib import Path

from pvcd import Ui_MainWindow

import functools


import numpy as np
from PIL import Image

from editor import Editor, VideoTransformDialog
from detector import *
from config import *

import time
import subprocess
from fractions import Fraction
import humanize


# from canvas import Canvas


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ######
        self.ui.pip_file_le.setText(DEFAULT_PIP_BACKGROUND)
        self.ui.logo_file_le.setText(DEFAULT_LOGO)
        ####

        self.query_viewer_size = (self.ui.query_image.width(), self.ui.query_image.height())
        self.detector = Detector()
        self.editor = Editor()

        self.setWindowTitle('Partial Video Copy Detection')

        # Fix window size
        default_size = QSize(1280, 720)
        self.setMinimumSize(default_size)
        self.setMaximumSize(default_size)

        header = self.ui.result_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)

        self.preview_size = (self.ui.preview_image.width(), self.ui.preview_image.height())

        # window title clicked and move
        self.ui.window.mouseMoveEvent = functools.partial(moveWindow, window=self)
        self.ui.win_close_btn.clicked.connect(lambda: self.close())
        self.ui.win_minimize_btn.clicked.connect(lambda: self.showMinimized())
        # self.ui.btn_maximize.clicked.connect(NotImplemented)  # maximize and restore => doesn't need
        self.setWindowFlags(Qt.FramelessWindowHint)  # hide basic window

        self.ui.page_1_btn.clicked.connect(
            functools.partial(self.btn_page_clicked, widget=self.ui.page_1, title='Detect Copy'))
        self.ui.page_2_btn.clicked.connect(
            functools.partial(self.btn_page_clicked, widget=self.ui.page_2, title='Edit Video'))

        #################
        # Page 1 Events
        #################
        self.ui.query_open_btn.clicked.connect(self.e_query_video_open_btn_clicked)
        self.ui.query_open_le.textChanged.connect(self.e_query_video_le_changed)
        self.ui.query_topk_slider.valueChanged.connect(
            functools.partial(self.e_change_label_by_slider,
                              slider=self.ui.query_topk_slider,
                              label=self.ui.query_topk_label))
        self.ui.query_wnd_slider.valueChanged.connect(
            functools.partial(self.e_change_label_by_slider,
                              slider=self.ui.query_wnd_slider,
                              label=self.ui.query_wnd_label))
        self.ui.query_score_thr_slider.valueChanged.connect(
            functools.partial(self.e_change_label_by_slider,
                              slider=self.ui.query_score_thr_slider,
                              label=self.ui.query_score_thr_label,
                              unit=0.01, format='{:.2f}'))
        self.ui.query_match_thr_slider.valueChanged.connect(
            functools.partial(self.e_change_label_by_slider,
                              slider=self.ui.query_match_thr_slider,
                              label=self.ui.query_match_thr_label))

        self.ui.query_reset_btn.clicked.connect(self.e_query_reset_btn_clicked)
        self.ui.query_submit_btn.clicked.connect(self.e_query_submit_btn_clicked)

        self.ui.result_table.doubleClicked.connect(self.e_query_result_dclicked)

        #################
        # Page 2 Events
        #################
        self.ui.preview_open_file_btn.clicked.connect(self.e_preview_file_open_btn_clicked)
        self.ui.bright_combo.currentIndexChanged.connect(self.e_bright_changed)
        self.ui.contrast_combo.currentIndexChanged.connect(self.e_contrast_changed)
        self.ui.rotate_combo.currentIndexChanged.connect(self.e_rotation_changed)
        self.ui.flip_combo.currentIndexChanged.connect(self.e_flip_changed)
        self.ui.fps_combo.currentIndexChanged.connect(self.e_fps_changed)
        self.ui.gray_combo.currentIndexChanged.connect(self.e_gray_changed)

        self.ui.crop_check.stateChanged.connect(self.e_crop_changed)
        self.ui.crop_slider.valueChanged.connect(self.e_crop_changed)
        # self.ui.crop_slider.sliderReleasvaed.connect(self.e_crop_slider_released) ..

        self.ui.border_check.stateChanged.connect(self.e_border_changed)
        self.ui.border_w_slider.valueChanged.connect(self.e_border_changed)
        self.ui.border_h_slider.valueChanged.connect(self.e_border_changed)

        self.ui.res_check.toggled.connect(self.e_resolution_changed)
        self.ui.res_preset_rb.toggled.connect(self.e_resolution_changed)
        self.ui.res_preset_combo.currentIndexChanged.connect(self.e_resolution_changed)
        self.ui.res_ratio_rb.toggled.connect(self.e_resolution_changed)
        self.ui.res_ratio_slider.valueChanged.connect(self.e_resolution_changed)

        self.ui.pip_check.stateChanged.connect(self.e_pip_changed)
        self.ui.pip_file_le.textChanged.connect(self.e_pip_changed)
        self.ui.pip_ratio_slider.valueChanged.connect(self.e_pip_changed)
        self.ui.pip_file_open_btn.clicked.connect(self.e_pip_file_open_btn_clicked)
        self.ui.pip_file_reset_btn.clicked.connect(self.e_pip_file_reset_btn_clicked)

        self.ui.logo_check.stateChanged.connect(self.e_logo_changed)
        self.ui.logo_file_le.textChanged.connect(self.e_logo_changed)
        self.ui.logo_size_slider.valueChanged.connect(self.e_logo_changed)
        self.ui.logo_pos_x_slider.valueChanged.connect(self.e_logo_changed)
        self.ui.logo_pos_y_slider.valueChanged.connect(self.e_logo_changed)
        self.ui.logo_file_open_btn.clicked.connect(self.e_logo_file_open_btn_clicked)
        self.ui.logo_file_reset_btn.clicked.connect(self.e_logo_file_reset_btn_clicked)

        self.ui.caption_check.stateChanged.connect(self.e_caption_changed)
        self.ui.caption_text_le.textChanged.connect(self.e_caption_changed)
        self.ui.caption_x_slider.valueChanged.connect(self.e_caption_changed)
        self.ui.caption_y_slider.valueChanged.connect(self.e_caption_changed)

        self.ui.caption_font_label.mousePressEvent = self.e_caption_font_btn_clicked
        self.ui.caption_color_label.mousePressEvent = self.e_caption_color_btn_clicked

        self.ui.reset_trn_btn.clicked.connect(self.e_reset_transform_btn_clicked)

        self.ui.save_trn_btn.clicked.connect(self.e_save_transform_btn_clicked)
        self.ui.detect_trn_btn.clicked.connect(self.e_detect_transform_btn_clicked)

        # start
        self.ui.page_1_btn.click()

        self.show()

    #################
    # Page 1
    #################

    def set_query_video(self, path):
        thumbnail = Editor.extract_thumbnail_(path)
        qthumbnail = Editor.to_QtPixmap(Editor.resize_thumbnail(thumbnail, self.query_viewer_size))
        self.ui.query_image.setPixmap(qthumbnail)
        self.ui.query_open_le.setText(path)
        self.detector.video = path

    def e_query_video_open_btn_clicked(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        path, _ = dialog.getOpenFileName(self, 'Select video', FILE_DIALOG_ROOT, VIDEO_EXTENSION_FILTER, )

        if path:
            self.set_query_video(path)

    def e_query_video_le_changed(self):
        self.ui.result_table.clearContents()

    def e_change_label_by_slider(self, *args, **kwargs):
        slider = kwargs.get('slider')
        label = kwargs.get('label')
        unit = kwargs.get('unit', 1)
        form = kwargs.get('format')

        value = slider.value() * slider.tickInterval() * unit
        label.setText(form.format(value) if form else str(value))

    def e_query_reset_btn_clicked(self):
        self.ui.query_topk_slider.setValue(DEFAULT_QUERY_TOPK)
        self.ui.query_wnd_slider.setValue(DEFAULT_QUERY_WND)
        self.ui.query_score_thr_slider.setValue(DEFAULT_QUERY_SCORE)
        self.ui.query_match_thr_slider.setValue(DEFAULT_QUERY_MATCH)

    def e_query_submit_btn_clicked(self):
        self.ui.result_table.clearContents()

        if self.detector.video:
            param = {"topk": int(self.ui.query_topk_label.text()),
                     "window": int(self.ui.query_wnd_label.text()),
                     "score_threshold": float(self.ui.query_score_thr_label.text()),
                     "match_threshold": int(self.ui.query_match_thr_label.text())}

            self.ui.query_submit_btn.setEnabled(False)
            self.request_worker = PostRequestWorker(self.receive_response,
                                                    PVCD_QUERY_POST_URL,
                                                    self.detector.video,
                                                    param)
            self.request_worker.start()
        else:
            error_dialog = QErrorMessage(self)
            error_dialog.showMessage('No input video')

    def receive_response(self, response):
        try:
            print(response)
            if response.status_code == 201:
                self.detector.response = response
                contents = self.detector.contents = response.json()

                self.ui.api.setText(f'<a href="{contents["url"]}" style="color: rgb(230,230,230);">API</a>')
                self.ui.json.setText(
                    f'<a href="{contents["url"]}?format=json" style="color: rgb(230,230,230);">JSON</a>')
                results = contents['results'][:DETECT_MAX_ROW]

                for r in results:
                    row = r['rank'] - 1
                    (rank, name, score, match, length) = (r['rank'],
                                                          os.path.basename(r['reference']['name']),
                                                          r['score'],
                                                          r['match'],
                                                          r['reference_end'] - r['reference_start'])
                    self.detector.results[row] = {'rank': rank,
                                                  'name': name,
                                                  'score': score,
                                                  'match': match,
                                                  'length': length}

                    # self.ui.result_table.setItem(row, 0, QTableWidgetItem(str(rank)))
                    self.ui.result_table.setItem(row, 0, QTableWidgetItem(str(name)))
                    self.ui.result_table.setItem(row, 1, QTableWidgetItem(f'{length} sec'))
                    self.ui.result_table.setItem(row, 2, QTableWidgetItem('{:.2f}'.format(score)))
                    self.ui.result_table.setItem(row, 3, QTableWidgetItem(str(match)))
            else:
                self.ui.api.setText(
                    f'<a href="{PVCD_QUERY_POST_URL}" style="color: rgb(230,230,230);">API</a>')
                self.ui.json.setText(
                    f'<a href="{PVCD_QUERY_POST_URL}/?format=json" style="color: rgb(230,230,230);">JSON</a>')
        finally:
            self.ui.query_submit_btn.setEnabled(True)

    def e_query_result_dclicked(self):
        row = self.ui.result_table.currentIndex().row()
        column = self.ui.result_table.currentIndex().column()

        if self.detector.results.get(row):
            print(row, column, self.detector.contents['results'][row])
            query = self.detector.contents['_video']
            result = self.detector.contents['results'][row]

            command1 = [POT_PLAYER_PATH,
                        query,
                        f'/seek={result["query_start"]}',
                        f'/title=Query'
                        ]
            command2 = [POT_PLAYER_PATH,
                        result['reference']['_video'],
                        f'/seek={result["reference_start"]}',
                        f'/title=Rank {result["rank"]}']

            self.p2 = Player(self.play, command2)
            self.p2.start()

            self.p1 = Player(self.play, command1)
            self.p1.start()

            # proc1 = subprocess.Popen(command1)
            # proc2 = subprocess.Popen(command2)

    def play(self, cmd):
        print(f'play {cmd}')

    #################
    # Page 2
    #################

    def e_bright_changed(self, idx):
        key = 'brightness'
        if idx != 3:
            self.editor.append_transform(key, {'value': int(self.ui.bright_combo.currentText())})
        else:
            self.editor.remove_transform(key)

        # repaint preview poster
        self.apply_thumbnail_transform()

    def e_contrast_changed(self, idx):
        key = 'contrast'
        if idx != 1:
            self.editor.append_transform(key, {'value': int(self.ui.contrast_combo.currentText())})
        else:
            self.editor.remove_transform(key)

        self.apply_thumbnail_transform()

    def e_rotation_changed(self, idx):
        key = 'rotate'
        if idx != 0:
            self.editor.append_transform(key, {'value': int(self.ui.rotate_combo.currentText())})
        else:
            self.editor.remove_transform(key)

        self.apply_thumbnail_transform()

    def e_flip_changed(self, idx):
        key = 'flip'
        if idx != 0:
            self.editor.append_transform(key, {'value': self.ui.flip_combo.currentText().lower()})
        else:
            self.editor.remove_transform(key)

        self.apply_thumbnail_transform()

    def e_fps_changed(self, idx):
        key = 'fps'
        if idx != 0:
            value = int(self.ui.fps_combo.currentText().split('fps')[0])
            self.editor.append_transform(key, {'value': value})
        else:
            self.editor.remove_transform(key)

        self.apply_thumbnail_transform()

    def e_gray_changed(self, idx):
        key = 'grayscale'
        if idx != 0:
            self.editor.append_transform(key, {'value': True})
        else:
            self.editor.remove_transform(key)

        self.apply_thumbnail_transform()

    def e_crop_changed(self, *args):
        key = 'crop'
        state = self.ui.crop_check.isChecked()
        value = self.ui.crop_slider.value() * self.ui.crop_slider.tickInterval()

        self.ui.crop_label.setText(f'{value} %' if value != 0 else 'Ratio')

        if state and value != 0:
            self.editor.append_transform(key, {'value': value})
        else:
            self.editor.remove_transform(key)

        self.apply_thumbnail_transform()

    def e_border_changed(self, *args):
        key = 'border'
        w = self.ui.border_w_slider.value() * self.ui.border_w_slider.tickInterval()
        h = self.ui.border_h_slider.value() * self.ui.border_h_slider.tickInterval()
        state = self.ui.border_check.isChecked()

        self.ui.border_w_label.setText(f'{w} %' if w != 0 else 'W')
        self.ui.border_h_label.setText(f'{h} %' if h != 0 else 'H')

        if state and not (w == 0 and h == 0):
            self.editor.append_transform(key, {'w': w, 'h': h})
        else:
            self.editor.remove_transform(key)
        self.apply_thumbnail_transform()

    def e_resolution_changed(self, *args):
        key = 'resolution'
        state = self.ui.res_check.isChecked()

        ratio_value = self.ui.res_ratio_slider.value() * self.ui.res_ratio_slider.tickInterval()
        self.ui.res_ratio_rb.setText(f'{ratio_value} %' if ratio_value != 0 else 'Ratio')
        param = {'ratio': ratio_value, 'preset': self.ui.res_preset_combo.currentText().lower()}

        if self.ui.res_preset_rb.isChecked():
            param['selector'] = 'preset'
        if self.ui.res_ratio_rb.isChecked():
            param['selector'] = 'ratio'

        if state and param.get('selector') \
                and ((param['selector'] == 'ratio' and param['ratio'] != 0)
                     or (param['selector'] == 'preset' and param['preset'] != 'none')):
            self.editor.append_transform(key, param)

        else:
            self.editor.remove_transform(key)

        self.apply_thumbnail_transform()

    def e_pip_changed(self, *args):
        key = 'pip'
        state = self.ui.pip_check.isChecked()
        bg = self.ui.pip_file_le.text()
        size = self.ui.pip_ratio_slider.value() * self.ui.pip_ratio_slider.tickInterval()

        self.ui.pip_ratio_label.setText(f'{size} %' if size != 0 else 'Ratio')

        if state and size != 0:
            self.editor.append_transform(key, {'background': bg, 'size': size})
        else:
            self.editor.remove_transform(key)
        self.apply_thumbnail_transform()

    def e_pip_file_open_btn_clicked(self):
        path, _ = QFileDialog.getOpenFileName(self, 'Select Background Image', FILE_DIALOG_ROOT, IMAGE_EXTENSION_FILTER)
        if path != '':
            self.ui.pip_file_le.setText(path)

    def e_pip_file_reset_btn_clicked(self):
        self.ui.pip_file_le.setText(DEFAULT_PIP_BACKGROUND)

    def e_logo_changed(self):
        key = 'logo'

        state = self.ui.logo_check.isChecked()
        file = self.ui.logo_file_le.text()
        size = self.ui.logo_size_slider.value() * self.ui.logo_size_slider.tickInterval()
        pos_x = self.ui.logo_pos_x_slider.value() * self.ui.logo_pos_x_slider.tickInterval()
        pos_y = self.ui.logo_pos_y_slider.value() * self.ui.logo_pos_y_slider.tickInterval()

        self.ui.logo_pos_x_label.setText(f'{pos_x} %' if pos_x != 0 else 'X')
        self.ui.logo_pos_y_label.setText(f'{pos_y} %' if pos_y != 0 else 'Y')
        self.ui.logo_size_label.setText(f'{size} %' if size != 0 else 'Size')

        if state and size != 0:
            self.editor.append_transform(key, {'logo': file, 'size': size, 'x': pos_x, 'y': pos_y})
        else:
            self.editor.remove_transform(key)

        self.apply_thumbnail_transform()

    def e_logo_file_open_btn_clicked(self):
        path, _ = QFileDialog.getOpenFileName(self, 'Select Logo Image', FILE_DIALOG_ROOT, IMAGE_EXTENSION_FILTER)
        if path != '':
            self.ui.logo_file_le.setText(path)

    def e_logo_file_reset_btn_clicked(self):
        self.ui.logo_file_le.setText(DEFAULT_LOGO)

    def e_caption_changed(self):
        key = 'caption'

        state = self.ui.caption_check.isChecked()
        text = self.ui.caption_text_le.text()
        pos_x = self.ui.caption_x_slider.value() * self.ui.caption_x_slider.tickInterval()
        pos_y = self.ui.caption_y_slider.value() * self.ui.caption_x_slider.tickInterval()
        font, size, *_ = self.ui.caption_font_label.text().split(',')
        color = self.ui.caption_color.text()

        self.ui.caption_x_label.setText(f'{pos_x} %' if pos_x != 0 else 'X')
        self.ui.caption_y_label.setText(f'{pos_y} %' if pos_y != 0 else 'Y')
        if state and text != '':
            self.editor.append_transform(key, {'text': text, 'font': font, 'size': int(size),
                                               'color': color, 'x': pos_x, 'y': pos_y})
        else:
            self.editor.remove_transform(key)

        self.apply_thumbnail_transform()

    def e_caption_font_btn_clicked(self, *args):
        prev = self.ui.caption_font_label.text()
        name, size, *_ = prev.split(',')

        code, font = QFontDialog.getFont(QFont(name, int(size)))
        if code:
            self.ui.caption_font_label.setText(f'{font.family()}, {font.pointSize()}')
            display_size = max(8, min(font.pointSize() // 2, 20))
            font.setPointSize(display_size)
            self.ui.caption_font_label.setFont(font)

            self.e_caption_changed()  # trigger

    def e_caption_color_btn_clicked(self, *args):
        prev = self.ui.caption_color.text()
        color = QColorDialog.getColor(QColor(prev))
        if color.isValid():
            self.ui.caption_color.setText(color.name())
            self.ui.caption_color_label.setStyleSheet(f'background-color:{color.name()};')

            self.e_caption_changed()  # trigger

    def apply_thumbnail_transform(self):
        print(self.editor.transforms)

        thumb = self.editor.get_thumbnail(self.preview_size)
        if thumb:
            pixmap = self.editor.to_QtPixmap(thumb)
            self.ui.preview_image.setPixmap(pixmap)

    #####################

    def e_reset_transform_btn_clicked(self):
        self.ui.bright_combo.setCurrentIndex(3)
        self.ui.contrast_combo.setCurrentIndex(1)
        self.ui.rotate_combo.setCurrentIndex(0)
        self.ui.flip_combo.setCurrentIndex(0)
        self.ui.fps_combo.setCurrentIndex(0)
        self.ui.gray_combo.setCurrentIndex(0)

        self.ui.crop_check.setCheckState(Qt.CheckState.Unchecked)
        self.ui.crop_slider.setValue(0)

        self.ui.border_check.setCheckState(Qt.CheckState.Unchecked)
        self.ui.border_w_slider.setValue(0)
        self.ui.border_h_slider.setValue(0)

        self.ui.res_check.setCheckState(Qt.CheckState.Unchecked)
        self.ui.res_preset_rb.setAutoExclusive(False)
        self.ui.res_preset_rb.setChecked(False)
        self.ui.res_preset_rb.setAutoExclusive(True)
        self.ui.res_preset_combo.setCurrentIndex(0)
        self.ui.res_ratio_rb.setAutoExclusive(False)
        self.ui.res_ratio_rb.setChecked(False)
        self.ui.res_ratio_rb.setAutoExclusive(True)
        self.ui.res_ratio_slider.setValue(0)

        self.ui.pip_check.setCheckState(Qt.CheckState.Unchecked)
        self.ui.pip_file_reset_btn.click()
        self.ui.pip_ratio_slider.setValue(0)

        self.ui.logo_check.setCheckState(Qt.CheckState.Unchecked)
        self.ui.logo_file_reset_btn.click()
        self.ui.logo_size_slider.setValue(0)
        self.ui.logo_pos_x_slider.setValue(0)
        self.ui.logo_pos_y_slider.setValue(0)

        self.ui.caption_check.setCheckState(Qt.CheckState.Unchecked)
        self.ui.caption_text_le.setText('')
        self.ui.caption_color.setText(DEFAULT_FONT_COLOR)
        self.ui.caption_font_label.setText(f'{DEFAULT_FONT}, {DEFAULT_FONT_SIZE}')
        self.ui.caption_x_slider.setValue(0)
        self.ui.caption_y_slider.setValue(0)

        self.editor.reset_transforms()

    def e_save_transform_btn_clicked(self):
        if not self.editor.video:
            error_dialog = QErrorMessage(self)
            error_dialog.showMessage('No input video')
        elif not len(self.editor.transforms):
            error_dialog = QErrorMessage(self)
            error_dialog.showMessage('No Transforms')
        else:

            path, _ = QFileDialog.getSaveFileName(self, 'Save path', FILE_DIALOG_ROOT + '\\' + DEFAULT_TRANSFORM_OUTPUT)

            if path:
                path = Path(path)
                log_path = path.parent.joinpath(f'{path.stem}.txt')
                command = self.editor.get_video_transform_command(path.as_posix())
                print(command)

                d = VideoTransformDialog(command,
                                         max_len=self.editor.metadata.get('framecount', 100),
                                         log=log_path.as_posix(),
                                         parent=self)
                d.showModal()

    def e_detect_transform_btn_clicked(self):
        if not self.editor.video:
            error_dialog = QErrorMessage(self)
            error_dialog.showMessage('No input video')
        elif not len(self.editor.transforms):
            error_dialog = QErrorMessage(self)
            error_dialog.showMessage('No Transforms')
        else:

            path, _ = QFileDialog.getSaveFileName(self, 'Save path', FILE_DIALOG_ROOT + '\\' + DEFAULT_TRANSFORM_OUTPUT)

            if path:
                path = Path(path)
                log_path = path.parent.joinpath(f'{path.stem}.txt')
                command = self.editor.get_video_transform_command(path.as_posix())
                print(command)

                d = VideoTransformDialog(command,
                                         max_len=self.editor.metadata.get('framecount', 100),
                                         log=log_path.as_posix(),
                                         parent=self)
                d.showModal()

                self.set_query_video(path.as_posix())
                self.ui.page_1_btn.click()

    def e_preview_file_open_btn_clicked(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        path, _ = dialog.getOpenFileName(self, 'Select video', FILE_DIALOG_ROOT, VIDEO_EXTENSION_FILTER, )

        if path:
            self.editor.video = path

            # parser metadata and get poster image
            self.editor.thumbnail = self.editor.extract_thumbnail()

            # update poster
            thumbnail = self.editor.get_thumbnail(self.preview_size)
            pixmap = self.editor.to_QtPixmap(thumbnail)
            self.ui.preview_image.setPixmap(pixmap)
            self.ui.preview_open_file_label.setText(path)

            # update_metadata
            meta = self.editor.metadata
            self.ui.meta_size_le.setText(f"{meta.get('width')} x {meta.get('height')}")
            self.ui.meta_nbframe_le.setText(f"{meta.get('framecount')}")
            self.ui.meta_fps_le.setText(f"{float(Fraction(meta.get('framerate'))):.2f}")
            self.ui.meta_duration_le.setText(f"{meta.get('duration'):.2f} sec")
            self.ui.meta_rotate_le.setText(f"{meta.get('rotate')}")
            self.ui.meta_filesize_le.setText(humanize.naturalsize(meta.get('size')))
            self.ui.meta_vc_le.setText(meta.get('video_codec'))
            self.ui.meta_ac_le.setText(meta.get('audio_codec'))
            self.ui.meta_format_le.setText(meta.get('format'))

    def btn_page_clicked(self, widget, title=''):
        self.ui.stackedWidget.setCurrentWidget(widget)
        if not isinstance(title, str):
            title = ' '
        self.ui.page_header.setText(title)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()  # monitor pos
        if event.buttons() == Qt.LeftButton:
            print(f'Mouse L_BTN_DOWN: {self.dragPos}')
        if event.buttons() == Qt.RightButton:
            print(f'Mouse R_BTN_DOWN: {self.dragPos}')
        if event.buttons() == Qt.MiddleButton:
            print(f'Mouse M_BTN_DOWN: {self.dragPos}')

    def keyPressEvent(self, event):
        print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))


def moveWindow(event, window):
    # # MOVE WINDOW
    if event.buttons() == Qt.LeftButton:
        window.move(window.pos() + event.globalPos() - window.dragPos)
        window.dragPos = event.globalPos()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()

    sys.exit(app.exec())
