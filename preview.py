#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, math
from PyQt4 import QtGui, QtCore
import preview_ui


# Shows the preview window showcasing the changes made in the editor window
class Preview(QtGui.QWidget) :

    closeApp = QtCore.pyqtSignal() #signal , slot to be with caller

    def __init__(self, ui):
        super(Preview, self).__init__()
        self.ui = ui
        self.font = self.color = self.image = None
        print "construction"
        

    def setup_connections(self) :
        self.ui.pushButton.clicked.connect( self.closeWidget )

    def moveStuff(self, scaleFactor, frameWidth, frameHeight, bannerCoords, bannerLabelCoords, bannerLabelText, font, color, image) :
        
        print scaleFactor["X"] * frameWidth
        # self.resize( scaleFactor["X"] * self.geometry().width(), scaleFactor["Y"] * self.geometry().height() )
        self.ui.bgLabel.resize( scaleFactor["X"] * frameWidth, scaleFactor["Y"] * frameHeight )
        
        self.ui.bannerlImage.setGeometry( bannerCoords )
        self.ui.bannerlImage.resize(scaleFactor["X"] * self.ui.bannerlImage.geometry().width(),  scaleFactor["Y"] * self.ui.bannerlImage.geometry().height())

        self.ui.bannerLabel.setGeometry( bannerLabelCoords )
        self.ui.bannerLabel.resize( scaleFactor["X"] * self.ui.bannerLabel.geometry().width(), scaleFactor["Y"] * self.ui.bannerLabel.geometry().height() )

        self.ui.bannerLabel.setText( bannerLabelText )
        if font is not None :
            self.font = font
            self.font.setPointSize( font.pointSize() *  int(math.sqrt( scaleFactor["X"] ** 2 + scaleFactor["Y"] ** 2 )  ) ) #don't know why I am using hypotenuse formula, seems to be the best bet right now
            self.ui.bannerLabel.setFont(self.font)
        if color is not None :
            self.color = color
            self.ui.bannerLabel.setStyleSheet("QLabel { color: %s}" % color.name())
        
        if image is not None :
            pixmap = QtGui.QPixmap( image )
            self.ui.bannerlImage.setPixmap( pixmap.scaled( scaleFactor["X"] * self.ui.bannerlImage.width(), scaleFactor["Y"] * self.ui.bannerlImage.height()))
            self.image = image
        
        self.ui.bannerLabel.raise_() #raise banner text on top of banner image

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

        def __del__(self):
            print "destruction"



    def closeWidget(self) :
        self.saveImage()
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


     
