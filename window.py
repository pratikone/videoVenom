import sys
import os
import basic_ui
import signals_slots
from timeline import AnotherTimeline, Communicate
from PyQt4 import QtGui, QtCore
from PyQt4.phonon import Phonon 

DELAY = 100 * 1 #  5 seconds in milli-seconds

class Window(QtGui.QMainWindow):


    def __init__(self):
        super(Window, self).__init__()
        self.ctr = 0
        self.c = Communicate() 
        self.timeline = AnotherTimeline( self, 600, {"w" : 450, "h" : 50, "x" : 280, "y" : 450} )
        self.signals_slots = signals_slots.Signal_Slots()

        #timer for animation
        #self.timer = QtCore.QTimer(self)
        #self.connect(self.timer,
        #             QtCore.SIGNAL("timeout()"),
        #             self.update)
        #self.timer.start(DELAY)
    
    def setup_connections( self, ui ) :
        ui.actionExit.triggered.connect(QtCore.QCoreApplication.instance().quit )
        ui.actionOpen.triggered.connect(lambda: self.signals_slots.open_file(self, ui))
        ui.playButton.clicked.connect(lambda: self.signals_slots.start_playback(self, ui))
        ui.stopButton.clicked.connect(lambda: self.signals_slots.stop_playback(self, ui))
        ui.seekSlider.setMediaObject(ui.videoPlayer.mediaObject())
        ui.volumeSlider.setAudioOutput(ui.videoPlayer.audioOutput())

        #ticker
        ui.videoPlayer.mediaObject().tick.connect(self.tick)
        self.c.updateBW[int].connect(self.timeline.setValue)



    def paintEvent(self, e):
        self.timeline.paintEvent(e )


   
    def tick(self, time):
        displayTime = QtCore.QTime(0, (time / 60000) % 60, (time / 1000) % 60).second()
        self.c.updateBW.emit(displayTime*60)        
        self.repaint()



def run():
    app = QtGui.QApplication(sys.argv)
    MainWindow = Window()
    ui = basic_ui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.setup_connections(ui)
    sys.exit(app.exec_())


run()