import sys

from PyQt5 import QtCore, QtWidgets, QtMultimedia

if __name__ == '__main__':
  def play_audio():
    app = QtWidgets.QApplication(sys.argv)
    filename = 'video/video.mp4'
    fullpath = QtCore.QDir.current().absoluteFilePath(filename) 
    url = QtCore.QUrl.fromLocalFile(fullpath)
    content = QtMultimedia.QMediaContent(url)
    player = QtMultimedia.QMediaPlayer()
    player.setMedia(content)
    player.play()
    sys.exit(app.exec_())

  def play_video():
    app = QtWidgets.QApplication(sys.argv)
    filename = '01 Somnus Orchestra.mp3'
    fullpath = QtCore.QDir.current().absoluteFilePath(filename) 
    url = QtCore.QUrl.fromLocalFile(fullpath)
    content = QtMultimedia.QMediaContent(url)
    player = QtMultimedia.QMediaPlayer()
    player.setMedia(content)
    player.play()
    sys.exit(app.exec_())
  

  play_audio()