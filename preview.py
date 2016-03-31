#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, math
from PyQt4 import QtGui, QtCore
import preview_ui
from vidGen import getFrameFromVideo


# Shows the preview window showcasing the changes made in the editor window
class Preview(QtGui.QWidget) :

    closeApp = QtCore.pyqtSignal() #signal , slot to be with caller

    def __init__(self, ui):
        super(Preview, self).__init__()
        self.ui = ui
        self.font = self.color = self.image = None
        

    def setup_connections(self) :
        self.ui.pushButton.clicked.connect( self.closeWidget )

    def moveStuff(self, scaleFactor, frameCoords, bannerCoords, bannerLabelCoords, bannerLabelText, font, color, image) :
        #resize whole widget
        self.resize( scaleFactor * frameCoords.width() + 30 , scaleFactor * frameCoords.height() + 30 )
        
        #resize video frame
        self.ui.bgLabel.resize( scaleFactor * frameCoords.width(), scaleFactor * frameCoords.height() )
        originalVideoLocation = self.caller.caller.file #calling main window
        if originalVideoLocation is not None :
            bgPixmap = QtGui.QPixmap( getFrameFromVideo( originalVideoLocation, 200 ) ) #make sure asked frame count is less than that of video
            self.ui.bgLabel.setPixmap( bgPixmap) 

        #resize banner image
        self.ui.bannerlImage.setGeometry( bannerCoords )
        diffX = abs(self.ui.bannerlImage.geometry().x() - frameCoords.x() )
        diffY = abs(self.ui.bannerlImage.geometry().y() - frameCoords.y() )
        self.ui.bannerlImage.setGeometry( frameCoords.x() + scaleFactor * diffX, \
                                          frameCoords.y() + scaleFactor * diffY, \
                                          scaleFactor * self.ui.bannerlImage.geometry().width(), \
                                          scaleFactor * self.ui.bannerlImage.geometry().height()  )

        #resize label
        self.ui.bannerLabel.setGeometry( bannerLabelCoords )

        diffX = abs(self.ui.bannerLabel.geometry().x() - frameCoords.x() )
        diffY = abs(self.ui.bannerLabel.geometry().y() - frameCoords.y() )
        self.ui.bannerLabel.setGeometry( frameCoords.x() + scaleFactor * diffX, \
                                          frameCoords.y() + scaleFactor * diffY, \
                                          scaleFactor * self.ui.bannerLabel.geometry().width(), \
                                          scaleFactor * self.ui.bannerLabel.geometry().height()  )

        self.ui.bannerLabel.setText( bannerLabelText )
        
        self.font = QtGui.QFont(font) 
        self.font.setPointSize( self.font.pointSize() * scaleFactor ) #resize font
        self.ui.bannerLabel.setFont(self.font)
        if color is not None :
            self.color = color
            self.ui.bannerLabel.setStyleSheet("QLabel { color: %s}" % color.name())
        
        if image is not None :
            pixmap = QtGui.QPixmap( image ) 
            self.ui.bannerlImage.setPixmap( pixmap.scaled( scaleFactor * self.ui.bannerlImage.width(), scaleFactor * self.ui.bannerlImage.height())) #resize image
            self.image = image
        
        self.ui.bannerLabel.raise_() #raise banner text on top of banner image

        #move OK button out of the way of the image. If it is not visible, user may exit with [X] button on top
        self.ui.pushButton.move( self.ui.pushButton.geometry().x(), self.ui.bgLabel.geometry().y() + self.ui.bgLabel.geometry().height() + 20 )
        self.repaint()


    def saveImage(self) :
        image =  QtGui.QImage(self.geometry().width(), self.geometry().height()  , QtGui.QImage.Format_ARGB32_Premultiplied);
        qp = QtGui.QPainter()
        qp.begin(image)
        # qp.fillRect(self.ui.bannerlImage.geometry(), Qt::yellow);
        # pix = QtGui.QPixmap(image)
        # qp.drawPixmap( QtCore.QRect(50, 50, 100, 100), pix, QtCore.QRect(50, 50, 100, 100) )
        if self.image is not None :
            qp.drawPixmap( self.ui.bannerlImage.geometry(), self.ui.bannerlImage.pixmap(),  self.ui.bannerlImage.pixmap().rect() )
            # qp.drawPixmap( self.ui.bannerlImage.geometry(), pix, self.ui.bannerlImage.geometry() )
        if self.font is not None :
            qp.setFont( self.font )
        if self.color is not None :
            qp.setPen(self.color)
        
        qp.drawText( self.ui.bannerLabel.geometry(), QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter,  self.ui.bannerLabel.text());
        image.save("output.png")
        qp.end()

    def closeEvent(self, event) :
        self.closeWidget()

    def closeWidget(self) :
        self.saveImage()
        self.closeApp.emit()
        self.close()



def showPreview( caller  ) :
    ui = preview_ui.Ui_Preview()
    widget = Preview( ui )
    ui.setupUi(widget)
    widget.setup_connections()
    widget.caller = caller
    widget.show()
    return widget



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    widget = showPreview(app)
    sys.exit(app.exec_())


     
