import sys
import os
import basic_ui
import signals_slots
from timeline import Timeline
from PyQt4 import QtGui, QtCore
from PyQt4.phonon import Phonon 

DELAY = 100 * 1 #  5 seconds in milli-seconds

class Window(QtGui.QMainWindow):


    def __init__(self):
        super(Window, self).__init__()
        self.ctr = 0
        self.timeline = Timeline()
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



    def paintEvent(self, e):
        print "paintEvent called"
        
        start = {"x" : 170, "y" : 410 }
        end = {"x" : 430, "y" : 500}
        lines = { "short" : 5, "long" : 12 }

        qp = QtGui.QPainter()
        qp.begin(self)
        self.timeline.drawRectangles(qp, start, end, lines)
        self.timeline.drawLines(qp, start, end, lines)

        self.timeline.drawTicker(qp, start, end, lines, self.ctr)

        qp.end()    


    #def update( self) :
    #    print "something"
    #    self.ctr = self.ctr + 1
    #    print self.ctr
    #    self.repaint()

    def tick(self, time):
        displayTime = QtCore.QTime(0, (time / 60000) % 60, (time / 1000) % 60).second()
        print displayTime * 10
        self.ctr = displayTime * 10
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