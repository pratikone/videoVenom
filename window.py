import sys
import os
import basic_ui
from timeline import AnotherTimeline, Communicate
from PyQt4 import QtGui, QtCore
from PyQt4.phonon import Phonon 
import textEditor

DELAY = 100 * 1 #  5 seconds in milli-seconds

class Window(QtGui.QMainWindow):


    def __init__(self):
        super(Window, self).__init__()
        self.c = Communicate() 
        self.timeline = AnotherTimeline( self, 600, {"w" : 450, "h" : 50, "x" : 280, "y" : 450} )
        self.bannerAndText = False
        self.bannerWidget = None
        #timer for animation
        #self.timer = QtCore.QTimer(self)
        #self.connect(self.timer,
        #             QtCore.SIGNAL("timeout()"),
        #             self.update)
        #self.timer.start(DELAY)
    
    def setup_connections( self, ui ) :
        self.ui = ui
        ui.actionExit.triggered.connect(QtCore.QCoreApplication.instance().quit )
        ui.actionOpen.triggered.connect(lambda: self.open_file(self, ui))
        ui.playButton.clicked.connect(lambda: self.start_playback(self, ui))
        ui.stopButton.clicked.connect(lambda: self.stop_playback(self, ui))
        ui.seekSlider.setMediaObject(ui.videoPlayer.mediaObject())
        ui.volumeSlider.setAudioOutput(ui.videoPlayer.audioOutput())
        ui.bannerBtn.clicked.connect(self.bannerToogle)
        #ticker
        ui.videoPlayer.mediaObject().tick.connect(self.tick)
        self.c.updateBW[int].connect(self.timeline.setValue)




    def paintEvent(self, e):
        self.timeline.paintEvent(e )


   
    def tick(self, time):
        displayTime = QtCore.QTime(0, (time / 60000) % 60, (time / 1000) % 60).second()
        print displayTime
        self.c.updateBW.emit(displayTime)        
        self.repaint()

    def open_file( self, window, ui) :
        file = QtGui.QFileDialog.getOpenFileName(window, 'Open movie file')
        unified_file = os.path.normpath(unicode(file)) 
        mediaSource = Phonon.MediaSource( unified_file )
        ui.videoPlayer.load( mediaSource )
        print unified_file


    def start_playback( self, window, ui ) :
        ui.videoPlayer.play()
        self.timeline.my_range = ui.videoPlayer.mediaObject().totalTime() / 1000  #converting millisecond to second
        print self.timeline.my_range


    def stop_playback( self, window, ui ) :
        ui.videoPlayer.stop()

    def bannerToogle(self) :
        if self.bannerAndText is False :
                self.bannerWidget = textEditor.showBannerandText()
                #banner and text
                self.bannerWidget.closeApp.connect( self.destroying_bannerWidget ) #connecting destructor to signal

                self.bannerAndText = True
                self.ui.bannerBtn.setText("Remove banner")
        elif self.bannerAndText is True :
                self.bannerAndText = False
                self.ui.bannerBtn.setText("Add banner")
        self.repaint()

    def destroying_bannerWidget(self) :
        self.bannerWidget = None
     


def run():
    app = QtGui.QApplication(sys.argv)
    MainWindow = Window()
    ui = basic_ui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.setup_connections(ui)
    sys.exit(app.exec_())


run()