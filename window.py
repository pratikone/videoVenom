import sys
import os
import basic_ui
from timeline import AnotherTimeline, Communicate
from PyQt4 import QtGui, QtCore
from PyQt4.phonon import Phonon 
import textEditor
import videoProcessing

DELAY = 100 * 1 #  5 seconds in milli-seconds

class Window(QtGui.QMainWindow):


    def __init__(self):
        super(Window, self).__init__()
        self.c = Communicate() 
        self.timeline = AnotherTimeline( self, 80, {"w" : 450, "h" : 50, "x" : 280, "y" : 450} )
        self.bannerAndText = False
        self.bannerWidget = None
        self.publishWidget = None
        self.file = None
        self.startTimeInSec = self.endTimeInSec = 0
    
    def setup_connections( self, ui ) :
        self.ui = ui
        ui.actionExit.triggered.connect(QtCore.QCoreApplication.instance().quit )
        ui.actionOpen.triggered.connect(self.open_file)
        ui.playButton.clicked.connect(self.start_playback)
        ui.pauseButton.clicked.connect(self.pause_playback)
        ui.stopButton.clicked.connect(self.stop_playback)
        ui.seekSlider.setMediaObject(ui.videoPlayer.mediaObject())
        ui.volumeSlider.setAudioOutput(ui.videoPlayer.audioOutput())
        ui.bannerBtn.clicked.connect(self.bannerToogle)
        ui.startTimeWidget.timeChanged.connect( self.moveBannerInTimeline )
        ui.endTimeWidget.timeChanged.connect( self.moveBannerInTimeline )
        ui.publishButton.clicked.connect( self.showPublishWidget )
        #ticker
        ui.videoPlayer.mediaObject().tick.connect(self.tick)
        self.c.updateBW[int].connect(self.timeline.setValue)




    def paintEvent(self, e):
        self.timeline.paintEvent(e )


   
    def tick(self, time):
        self.timeline.my_range = self.ui.videoPlayer.mediaObject().totalTime() / 1000  #converting millisecond to second
        if self.errorConditionsBannerTime() is True : #check for errors
            return

        # video width and height
        self.videoWidth = self.ui.videoPlayer.videoWidget().sizeHint().width()
        self.videoHeight = self.ui.videoPlayer.videoWidget().sizeHint().height()

        displayTime = time / 1000  #seconds
        self.c.updateBW.emit(displayTime)        
        self.repaint()

    def open_file( self) :
        file = QtGui.QFileDialog.getOpenFileName(self, 'Open movie file')
        self.file = os.path.normpath(unicode(file)) 
        mediaSource = Phonon.MediaSource( self.file )
        self.ui.videoPlayer.load( mediaSource )
        print self.file
        self.start_playback() #start playback auto so that video data gets populated.


    def start_playback( self) :
        self.ui.videoPlayer.play()

    def pause_playback( self) :
        self.ui.videoPlayer.pause()

    def stop_playback( self) :
        self.ui.videoPlayer.stop()

    def moveBannerInTimeline(self) : 
        if self.errorConditionsBannerTime( takeAction = False ) is False : 
            self.startTimeInSec = self.ui.startTimeWidget.time().hour() * 3600 + self.ui.startTimeWidget.time().minute() * 60 + self.ui.startTimeWidget.time().second()
            self.endTimeInSec = self.ui.endTimeWidget.time().hour() * 3600 + self.ui.endTimeWidget.time().minute() * 60 + self.ui.endTimeWidget.time().second()
            self.timeline.setBannerDuration( self.startTimeInSec, self.endTimeInSec )
            self.repaint()


    def bannerToogle(self) :
        if self.bannerAndText is False :
                self.bannerWidget = textEditor.showBannerandText( self)
                self.bannerWidget.setScaleFactor( self.videoWidth, self.videoHeight )
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
     

    def showPublishWidget(self):
        self.publishWidget = videoProcessing.showProcessing( videoLocation = self.file, numVideos=1, \
                                        t1=self.startTimeInSec, t2=self.endTimeInSec, x=0, y=0, ImageLocation="output.png")
        self.publishWidget.closeApp.connect( self.destroyPublishWidget ) #connecting destructor to signal

    def destroyPublishWidget(self):
        self.publishWidget = None
    
    def errorConditionsBannerTime(self, takeAction = True) :
        if any( [ self.ui.startTimeWidget.time() > QtCore.QTime(0,0,0,0).addMSecs(self.timeline.my_range * 1000), self.ui.endTimeWidget.time() > QtCore.QTime(0,0,0,0).addMSecs(self.timeline.my_range * 1000 )] ) :
               if takeAction is True :
                   self.stop_playback()
                   print "Error. Start or End time for banner is more than video's length."
                   QtGui.QMessageBox.critical(self, "Error in playback", "Start or End time for banner is more than video's length.")
               return True
        
        if any( [ self.ui.startTimeWidget.time() > self.ui.endTimeWidget.time()] ) :
               if takeAction is True :
                   self.stop_playback()
                   print "Error. Start time cannot be more than the  End time."
                   QtGui.QMessageBox.critical(self, "Error in playback", " Start time cannot be more than the  End time.")
               return True

        return False

    def closeEvent(self, event) :
        if self.bannerWidget is not None :
            self.bannerWidget.closeEvent(event)
        if self.publishWidget is not None :
            self.publishWidget.closeEvent(event)


def run():
    app = QtGui.QApplication(sys.argv)
    MainWindow = Window()
    ui = basic_ui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.setup_connections(ui)
    sys.exit(app.exec_())


run()