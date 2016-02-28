#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore
import banner_ui
from size_handler import SizeHandler





class Widget(QtGui.QWidget) :


    start = {"x" : 50, "y" : 100 }
    end = {"x" : 300, "y" : 300 }

    def __init__(self, ui, sizeHandler = None):
        super(Widget, self).__init__()
        self.ui = ui
        self.sizeHandler = sizeHandler


    def initUI(self):      
        self.ui.bannerText.connect(self.ui.bannerText, QtCore.SIGNAL("textChanged(QString)"),
                    self.labelUpdate)
        self.ui.fontBtn.clicked.connect(self.font_choice)
        self.ui.colorBtn.clicked.connect(self.color_choice)
        
        self.bounds = QtCore.QRect(50, 100, 250, 200)
        self.setMouseTracking(True)  #mouse move will always be called, unlike earlier when it meant drag


        

    def labelUpdate(self):
        self.ui.bannerLabel.setText(self.ui.bannerText.text())

    def font_choice(self):
        font, valid = QtGui.QFontDialog.getFont()
        if valid:
            self.ui.bannerLabel.setFont(font)

    def color_choice(self):
        color = QtGui.QColorDialog.getColor()
        self.ui.bannerLabel.setStyleSheet("QLabel { color: %s}" % color.name())
            


    def paintEvent(self, e):
        if self.sizeHandler is not None and self.sizeHandler.object == "rectangle" :
            self.bounds = self.sizeHandler.bounds

        qp = QtGui.QPainter()
        qp.begin(self)
        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#d4d4d4')
        qp.setPen(color)
        qp.setBrush(QtGui.QColor("Red"))
        qp.drawRect(  self.bounds )
        qp.end()

        if self.sizeHandler is not None :
            self.sizeHandler.paintEvent( event)

    def mousePressEvent(self, event):
        print "yo"
        if self.bounds.contains( event.pos()) :
            if self.sizeHandler is None or self.sizeHandler.bounds != self.bounds : #selection
                self.sizeHandler = SizeHandler(self, "rectangle", self.bounds)
            self.sizeHandler.mousePressEvent(event)

        elif self.ui.bannerLabel.geometry().contains( event.pos() ) :
            if self.sizeHandler is None or self.sizeHandler.bounds != self.ui.bannerLabel.geometry() :
                self.sizeHandler = SizeHandler(self, self.ui.bannerLabel)
                self.sizeHandler.enable_Hresize = self.sizeHandler.enable_Vresize = False  #disabling handlers
            self.sizeHandler.mousePressEvent(event)

        self.repaint()
   
    def mouseReleaseEvent(self, event):
        print "yeah"
        if self.sizeHandler is not None :
            self.sizeHandler.mouseReleaseEvent(event)

    def mouseMoveEvent(self, event):
        if self.sizeHandler is not None :
            self.sizeHandler.mouseMoveEvent(event)
            if self.sizeHandler.can_Hresize is True or \
                self.sizeHandler.can_Vresize is True or \
                self.sizeHandler.can_move is True:

                self.repaint()
      


def main():
    
    app = QtGui.QApplication(sys.argv)
    ui = banner_ui.Ui_Form()
    widget = Widget(ui)
    ui.setupUi(widget)
    widget.initUI()
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
