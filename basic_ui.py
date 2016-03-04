# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pratika/Documents/github/videoVenom/ui/basic.ui'
#
# Created: Fri Mar  4 11:02:11 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(792, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.videoPlayer = phonon.Phonon.VideoPlayer(self.centralwidget)
        self.videoPlayer.setGeometry(QtCore.QRect(281, 11, 439, 281))
        self.videoPlayer.setStyleSheet(_fromUtf8("background-color: rgba(0, 0, 0, 100)"))
        self.videoPlayer.setObjectName(_fromUtf8("videoPlayer"))
        self.seekSlider = phonon.Phonon.SeekSlider(self.centralwidget)
        self.seekSlider.setGeometry(QtCore.QRect(280, 330, 441, 20))
        self.seekSlider.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 100)"))
        self.seekSlider.setObjectName(_fromUtf8("seekSlider"))
        self.volumeSlider = phonon.Phonon.VolumeSlider(self.centralwidget)
        self.volumeSlider.setGeometry(QtCore.QRect(610, 300, 109, 21))
        self.volumeSlider.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 100)"))
        self.volumeSlider.setObjectName(_fromUtf8("volumeSlider"))
        self.bannerBtn = QtGui.QPushButton(self.centralwidget)
        self.bannerBtn.setGeometry(QtCore.QRect(70, 270, 131, 41))
        self.bannerBtn.setObjectName(_fromUtf8("bannerBtn"))
        self.logoLabel = QtGui.QLabel(self.centralwidget)
        self.logoLabel.setGeometry(QtCore.QRect(10, 10, 241, 221))
        self.logoLabel.setObjectName(_fromUtf8("logoLabel"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(360, 370, 269, 28))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.playButton = QtGui.QPushButton(self.widget)
        self.playButton.setObjectName(_fromUtf8("playButton"))
        self.horizontalLayout.addWidget(self.playButton)
        self.pauseButton = QtGui.QPushButton(self.widget)
        self.pauseButton.setObjectName(_fromUtf8("pauseButton"))
        self.horizontalLayout.addWidget(self.pauseButton)
        self.stopButton = QtGui.QPushButton(self.widget)
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.horizontalLayout.addWidget(self.stopButton)
        self.widget1 = QtGui.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(10, 320, 241, 41))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.startTimeWidget = QtGui.QTimeEdit(self.widget1)
        self.startTimeWidget.setObjectName(_fromUtf8("startTimeWidget"))
        self.horizontalLayout_2.addWidget(self.startTimeWidget)
        self.endTimeWidget = QtGui.QTimeEdit(self.widget1)
        self.endTimeWidget.setObjectName(_fromUtf8("endTimeWidget"))
        self.horizontalLayout_2.addWidget(self.endTimeWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 792, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.bannerBtn.setText(_translate("MainWindow", "Banner and Text", None))
        self.logoLabel.setText(_translate("MainWindow", "Video Venom logo", None))
        self.playButton.setText(_translate("MainWindow", "Play", None))
        self.pauseButton.setText(_translate("MainWindow", "Pause", None))
        self.stopButton.setText(_translate("MainWindow", "Stop", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))

from PyQt4 import phonon

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

