#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, math, time
import threading
from PyQt4 import QtGui, QtCore
import processing_ui
import vidGen


DELAY = 100 #  1 second in milli-seconds

# Shows the preview window showcasing the changes made in the editor window
class Processing(QtGui.QWidget) :

    closeApp = QtCore.pyqtSignal() #signal , slot to be with caller

    def __init__(self, ui):
        super(Processing, self).__init__()
        self.ui = ui
        self.signals = callbackProcessing( self )

        

    def setup_connections(self) :
        self.ui.loadingLabel.resize(self.ui.loadingLabel.width() * 2, self.ui.loadingLabel.height())
        self.dontAnimate = False
        self.ui.animatedDial.setRange(0, 360)
        self.ui.animatedDial.setValue(0)
        self.timer = QtCore.QTimer(self)
        self.connect(self.timer,
                     QtCore.SIGNAL("timeout()"),
                     self.animate)
        self.timer.start(DELAY)

    def animate(self) :
        if self.dontAnimate is True :
            return
        val = self.ui.animatedDial.value()
        val = val + 10
        if val >= 360 :
            val = 0
        self.ui.animatedDial.setValue(val)
        
    def setText(self, text) :
        self.ui.loadingLabel.setText( text )


    def closeEvent(self, event) :
        self.closeWidget()

    def closeWidget(self) :
        self.closeApp.emit()
        self.close()


def showProcessing( videoLocation, numVideos=1, t1=0, t2=0, x=0, y=0, ImageLocation=None  ) :
    ui = processing_ui.Ui_Dialog()
    widget = Processing( ui )
    ui.setupUi(widget)
    widget.setup_connections()
    widget.show()

    t = threading.Thread(target=createVideos, args = (widget, videoLocation, numVideos, t1, t2, x, y, ImageLocation, widget.signals.videoProgressSignal))
    t.start()
    # createVideos( widget, videoLocation, numVideos, t1, t2, x, y, ImageLocation, widget.signals.videoProgressSignal )
    return widget

def createVideos( widget, videoLocation, numVideos=1, t1=0, t2=0, x=0, y=0, ImageLocation=None, callback=None ) :
    # ImageLocation = "C:/Users/pratika/Documents/GitHub/video venom/output.png"
    print "start"
    vidGen.GenerateTheVideo(str(videoLocation), numVideos, t1, t2, x, y, ImageLocation, callback ) #path where the video is located in string from unicode
    widget.setText("Completed")
    widget.dontAnimate = True
    widget.ui.animatedDial.setValue(0)

class callbackProcessing() :

   def __init__(self, widget):
        self.widget = widget
        
        
   def videoProgressSignal( self,videoNum ) :
        print "yo here"
        self.hello(videoNum)
        

   def hello( self, i) :
        print "hello hello" + str(i + 1)
        self.widget.setText("Processing video " + str(i+1))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    widget = showProcessing( "C:/Users/pratika/Desktop/valve.avi", 2 )
    
    sys.exit(app.exec_())


     
