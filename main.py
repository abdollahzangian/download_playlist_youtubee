import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from pytube import Playlist
import subprocess
import time


class Ui_Program(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_Program, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(300, 200)
        self.setWindowTitle('YouTube Playlist Downloader')
        self.url_label = QtWidgets.QLabel('Enter the YouTube playlist URL:', parent=self)
        self.url_label.move(30, 30)
        self.url_input = QtWidgets.QLineEdit(parent=self)
        self.url_input.setGeometry(30, 60, 240, 30)
        self.download_button = QtWidgets.QPushButton('Download', parent=self)
        self.download_button.setGeometry(100, 120, 100, 35)
        self.download_button.clicked.connect(self.download)

    def download(self):
        playlist_url = self.url_input.text()
        playlist = Playlist(playlist_url)
        print(f'Title: {playlist.title}')
        print(f'Number of videos in playlist: {len(playlist.video_urls)}') 
        for video_url in playlist.video_urls:
            print(f'Downloading {video_url}')
            subprocess.call(['C:\\Program Files (x86)\\Internet Download Manager\\IDMan.exe', '/d', video_url, '/n', '/a'])
            print(1)
            


qt_app = QtWidgets.QApplication(sys.argv)
program = Ui_Program()
program.show()
sys.exit(qt_app.exec_())




