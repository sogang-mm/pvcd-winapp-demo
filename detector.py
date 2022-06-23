from PySide6.QtCore import Qt, QThread
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QDialog

import requests
from config import *


class Detector:
    def __init__(self):
        self._video = None
        self.response = None
        self.contents = None
        self.results = dict()

    @property
    def video(self):
        return self._video

    @video.setter
    def video(self, path):
        self.reset_video()
        self._video = path

    def reset_video(self):
        self._video = None
        self.response = None
        self.contents = None
        self.results = dict()


class PostRequestWorker(QThread):

    def __init__(self, receiver, url, video, param):
        super(PostRequestWorker, self).__init__()
        self.receiver = receiver
        self.url = url
        self.form = {'files': {'video': video},
                     'data': param}

    def run(self):
        response = None
        try:
            if self.form:
                path = self.form['files']['video']
                self.form['files']['video'] = open(path, 'rb')
                response = requests.post(self.url, **self.form, timeout=PVCD_QUERY_TIME_OUT)
        finally:
            self.receiver(response)

    def stop(self):
        self.quit()


import subprocess


class Player(QThread):
    def __init__(self, receiver, cmd):
        super(Player, self).__init__()
        self.cmd = cmd
        self.receiver = receiver

    def run(self):
        proc = subprocess.Popen(self.cmd, stdout=subprocess.PIPE)
        self.receiver(self.cmd)
