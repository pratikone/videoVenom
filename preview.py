#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore
import preview_ui


# Shows the preview window showcasing the changes made in the editor window
class Preview(QtGui.QWidget) :

    closeApp = QtCore.pyqtSignal() #signal , slot to be with caller

    def __init__(self, ui):
        super(Preview, self).__init__()
        self.ui = ui
        

    def setup_connections(self) :
        self.ui.pushButton.clicked.connect( self.closeWidget )

    def moveStuff(self, scaleFactor, bannerCoords, bannerLabelCoords, bannerLabelText, font, color, image) :
        self.ui.bannerlImage.setGeometry( bannerCoords )
        self.ui.bannerlImage.geometry().setWidth( scaleFactor * self.ui.bannerlImage.geometry().width() )
        self.ui.bannerlImage.geometry().setHeight( scaleFactor * self.ui.bannerlImage.geometry().height() )

        self.ui.bannerLabel.setGeometry( bannerLabelCoords )
        self.ui.bannerLabel.geometry().setWidth( scaleFactor * self.ui.bannerLabel.geometry().width() )
        self.ui.bannerLabel.geometry().setHeight( scaleFactor * self.ui.bannerLabel.geometry().height() )

        self.ui.bannerLabel.setText( bannerLabelText )
        if font is not None :
            self.ui.bannerLabel.setFont(font)
        if color is not None :
            self.ui.bannerLabel.setStyleSheet("QLabel { color: %s}" % color.name())
        
        if image is not None :
            pixmap = QtGui.QPixmap( image )
            self.ui.bannerlImage.setPixmap( pixmap.scaled( self.ui.bannerlImage.width(), self.ui.bannerlImage.height()))
        
        self.ui.bannerLabel.raise_() #raise banner text on top of banner image

        self.repaint()

    def closeWidget(self) :
        self.closeApp.emit()
        self.close()


def showPreview(  ) :
    ui = preview_ui.Ui_Preview()
    widget = Preview( ui )
    ui.setupUi(widget)
    widget.setup_connections()

    widget.show()
    return widget



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    widget = showPreview()
    sys.exit(app.exec_())


     
