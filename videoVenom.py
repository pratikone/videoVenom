import sys
import os
# os.putenv("IMAGEIO_FFMPEG_EXE", os.getcwd() + 'ffmpeg.win32.exe')
# os.environ['IMAGEIO_FFMPEG_EXE'] = os.getcwd() + '/moviepy/ffmpeg.win32.exe'


import wizard_ui
from timeline import AnotherTimeline, Communicate
from PyQt4 import QtGui, QtCore
from PyQt4.phonon import Phonon 
# import qdarkstyle



DELAY = 100 * 1 #  5 seconds in milli-seconds

class Window(QtGui.QStackedWidget):


    def __init__(self):
        super(Window, self).__init__()
    
    def setup_connections( self, ui ) :
        self.ui = ui
        self.setCurrentIndex(1)
        self.ui.nextButton_4.clicked.connect(self.__next_page)



    def paintEvent(self, e):
        pass

    def __next_page(self):
        idx = self.currentIndex()
        if idx < self.count() - 1:
            self.setCurrentIndex(idx + 1)
        else:
            self.setCurrentIndex(0)



def run():
    app = QtGui.QApplication(sys.argv)
    # setup stylesheet
    # app.setStyleSheet(qdarkstyle.load_stylesheet(pyside=False))
    MainWindow = Window()
    ui = wizard_ui.Ui_StackedWidget()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.setup_connections(ui)
    sys.exit(app.exec_())


run()