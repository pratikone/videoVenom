#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, os
from PyQt4 import QtGui, QtCore


class Widget(QtGui.QWidget) :

    

    def __init__(self):
        super(Widget, self).__init__()
        self.initUI()
        self.setMouseTracking(True)  #mouse move will always be called, unlike earlier when it meant drag
        

    def initUI(self, sizeHandler = None):      
        self.setGeometry(300, 500, 350, 300)
        self.setWindowTitle('Colours')
        self.sizeHandler = sizeHandler
        self.bounds = QtCore.QRect(50, 100, 250, 200)
        self.label = QtGui.QLabel(self)
        #self.pixmap = QtGui.QPixmap( os.getcwd() + "/resources/pattern.jpg" )
        #self.label.setPixmap( self.pixmap.scaled( self.label.width(), self.label.height()))
        self.label.setText( " mann ke manjira baaje re " )
        self.label.move( 50, 20 )
        self.show()

    def paintEvent(self, event):

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
        if self.bounds.contains( event.pos()) :
            if self.sizeHandler is None or self.sizeHandler.bounds != self.bounds : #selection
                self.sizeHandler = SizeHandler(self, "rectangle", self.bounds)
            self.sizeHandler.mousePressEvent(event)

        elif self.label.geometry().contains( event.pos() ) :
            if self.sizeHandler is None or self.sizeHandler.bounds != self.label.geometry() :
                self.sizeHandler = SizeHandler(self, self.label)
                self.sizeHandler.enable_Hresize = self.sizeHandler.enable_Vresize = False  #disabling handlers
            self.sizeHandler.mousePressEvent(event)

        self.repaint()

    def mouseReleaseEvent(self, event):
        if self.sizeHandler is not None :
            self.sizeHandler.mouseReleaseEvent(event)

    def mouseMoveEvent(self, event):
        if self.sizeHandler is not None :
            self.sizeHandler.mouseMoveEvent(event)
            if self.sizeHandler.can_Hresize is True or \
                self.sizeHandler.can_Vresize is True or \
                self.sizeHandler.can_move is True:

                self.repaint()
        

class SizeHandler :

    HANDLER_XSIZE = 10
    HANDLER_YSIZE = 10

    def __init__(self, widget, obj, bounds=None) :
        self.object = obj  # could be any QPainter shape or Qlabel
        self.widget = widget
        if bounds is not None :
            self.bounds = bounds #in case of QPainter rectangle
        else :
            self.bounds = obj.geometry() # incase of QLabel and other UI elements

        self.can_Hresize = self.can_Vresize = self.can_move = False
        
        self.enable_Hresize = self.enable_Vresize = self.enable_move = True  # knobs to disable any of the handlers

        self.VBounds = QtCore.QRect( self.bounds.x() + self.bounds.width()/2 - self.HANDLER_XSIZE / 2 , self.bounds.y() , self.HANDLER_XSIZE, self.HANDLER_YSIZE)
        self.HBounds = QtCore.QRect( self.bounds.x() + self.bounds.width() - self.HANDLER_XSIZE, self.bounds.y() + self.bounds.height()/2 - self.HANDLER_YSIZE / 2, self.HANDLER_XSIZE, self.HANDLER_YSIZE)
        self.CBounds = QtCore.QRect( self.bounds.x() + self.bounds.width()/2 - self.HANDLER_XSIZE / 2, self.bounds.y() + self.bounds.height()/2 - self.HANDLER_YSIZE / 2, self.HANDLER_XSIZE, self.HANDLER_YSIZE)




    def paintEvent( self, event ) :
        qp = QtGui.QPainter()
        qp.begin(self.widget)
        
        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#d4d4d4')
        qp.setPen(color)
        # vertical  handle 
        self.VBounds = QtCore.QRect( self.bounds.x() + self.bounds.width()/2 - self.HANDLER_XSIZE / 2, self.bounds.y() , self.HANDLER_XSIZE, self.HANDLER_YSIZE)
        qp.setBrush(QtGui.QColor("Yellow"))
        if self.enable_Vresize is True :
            qp.drawRect(  self.VBounds )


        # horizontal  handle 
        self.HBounds = QtCore.QRect( self.bounds.x() + self.bounds.width() - self.HANDLER_XSIZE, self.bounds.y() + self.bounds.height()/2 - self.HANDLER_YSIZE / 2, self.HANDLER_XSIZE, self.HANDLER_YSIZE)
        qp.setBrush(QtGui.QColor("Yellow"))
        if self.enable_Hresize is True :
            qp.drawRect( self.HBounds ) 


        # central  handle 
        self.CBounds = QtCore.QRect( self.bounds.x() + self.bounds.width()/2 - self.HANDLER_XSIZE / 2, self.bounds.y() + self.bounds.height()/2 - self.HANDLER_YSIZE / 2, self.HANDLER_XSIZE, self.HANDLER_YSIZE)
        qp.setBrush(QtGui.QColor("Yellow"))
        if self.enable_move is True :
            qp.drawRect( self.CBounds ) 


        qp.end()    

    def mousePressEvent(self, event):
        #horizontal
        if self.enable_Hresize and self.HBounds.contains( event.pos()) :
                self.can_Hresize = True
        #vertical
        elif self.enable_Vresize and self.VBounds.contains( event.pos()) :
                self.can_Vresize = True
                
        elif self.enable_move and self.CBounds.contains( event.pos()) :
                self.can_move = True

                

    def mouseReleaseEvent(self, event):
        if self.can_Hresize == True :
            self.can_Hresize  = False

        elif self.can_Vresize == True :
            self.can_Vresize  = False
        
        elif self.can_move == True :
            self.can_move  = False

    def mouseMoveEvent(self, event):
        print "reacjing fn cstart"
        if self.can_Hresize == True:
            self.bounds.setRight(event.pos().x()) #change width of rectangle being drawn using these values
            if self.object == "rectangle" :
                pass  #nothing more is needed to be done here. PaintEvent takes care of everything
            else:
                self.widget.label.setGeometry( self.bounds )

        elif self.can_Vresize == True:
            self.bounds.setTop(event.pos().y())  #change height Qt is awesome for giving these functions
            if self.object == "rectangle" :
                pass
            else :
                self.widget.label.setGeometry( self.bounds )
        
        elif self.can_move == True:
                self.bounds = QtCore.QRect(event.pos().x() - self.bounds.width() / 2, \
                                            event.pos().y() - self.bounds.height() / 2, \
                                            self.bounds.width(), self.bounds.height()) 
                if self.object == "rectangle" :
                    pass
                else :
                    self.widget.label.setGeometry( self.bounds )
        
        else : #when mouse is simply moving and hovers over handlers, change mouse cursor momentarily
            print "reacjing ELSE"
            if self.HBounds.contains( event.pos()) :
                self.widget.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor )) #horizontal cursor

            elif self.VBounds.contains( event.pos()) :
                self.widget.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor )) #vertical cursor

            elif self.CBounds.contains( event.pos()) :
                print "reaching central"
                self.widget.setCursor(QtGui.QCursor(QtCore.Qt.SizeAllCursor )) #move cursor
            else:
                self.widget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor ))  #restore normal cursor


        #repaint to be called by the caller

def main():
    
    app = QtGui.QApplication(sys.argv)
    widget = Widget()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()