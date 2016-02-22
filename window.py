import sys
import os
import basic_ui
import signals_slots
from PyQt4 import QtGui, QtCore
from PyQt4.phonon import Phonon 

class Window(QtGui.QMainWindow):


    def __init__(self):
        super(Window, self).__init__()
        self.signals_slots = signals_slots.Signal_Slots()
    
    def setup_connections( self, ui ) :
        ui.actionExit.triggered.connect(QtCore.QCoreApplication.instance().quit )
        ui.actionOpen.triggered.connect(lambda: self.signals_slots.open_file(self, ui))
        ui.playButton.clicked.connect(lambda: self.signals_slots.start_playback(self, ui))
        ui.stopButton.clicked.connect(lambda: self.signals_slots.stop_playback(self, ui))




def run():
    app = QtGui.QApplication(sys.argv)
    MainWindow = Window()
    ui = basic_ui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.setup_connections(ui)
    sys.exit(app.exec_())


run()