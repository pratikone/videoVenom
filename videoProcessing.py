#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, math
import thread
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

        

    def setup_connections(self) :
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


def showProcessing(  ) :
    ui = processing_ui.Ui_Dialog()
    widget = Processing( ui )
    ui.setupUi(widget)
    widget.setup_connections()

    widget.show()
    return widget

def completion( widget, text ) :
    vidGen.GenerateTheVideo("/home/pratika/Downloads/my_composition.mp4" ) #path where the video is located
    widget.setText("Completed")
    widget.dontAnimate = True
    widget.ui.animatedDial.setValue(0)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    widget = showProcessing()
    completion(widget, "yo yo")
    sys.exit(app.exec_())


     
