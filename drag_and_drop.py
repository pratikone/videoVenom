#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore

DELAY = 100 * 1 #  5 seconds in milli-seconds




class Widget(QtGui.QWidget) :


    start = {"x" : 50, "y" : 100 }
    end = {"x" : 300, "y" : 300 }

    def __init__(self):
        super(Widget, self).__init__()
        self.initUI()
        self.can_Hresize = False
        self.can_Vresize = False

    def initUI(self):      
        self.setGeometry(300, 500, 350, 300)
        self.setWindowTitle('Colours')
        self.setAcceptDrops(True)
        self.show()

    def paintEvent(self, e):
        
        lines = { "short" : 5, "long" : 12 }

        width  = self.end["x"] - self.start["x"]
        height = self.end["y"] - self.start["y"]

        qp = QtGui.QPainter()
        qp.begin(self)
        
        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#d4d4d4')
        qp.setPen(color)

        # white
        qp.setBrush(QtGui.QColor("Red"))
        qp.drawRect( self.start["x"] - 2, self.start["y"] - 2, width, height)
        
        
        #horizontal handle
        self.x_Hcontainer = ( self.end["x"] - 4, self.end["x"] - 4 + 8  )
        self.y_Hcontainer = ( self.start["y"] + height/2 -4, self.start["y"] + height/2 -4 + 8  )
        qp.setBrush(QtGui.QColor("Black"))
        qp.drawRect( self.x_Hcontainer[0], self.y_Hcontainer[0] ,
                         self.x_Hcontainer[1] - self.x_Hcontainer[0], self.y_Hcontainer[1] - self.y_Hcontainer[0] )

        #vertical handle
        self.x_Vcontainer = ( self.start["x"] - 4 + width/2 -4 , self.start["x"] - 4 + width/2 + 4   )
        self.y_Vcontainer = ( self.start["y"] - 4, self.start["y"] + 4 )
        qp.setBrush(QtGui.QColor("Black"))
        qp.drawRect( self.x_Vcontainer[0], self.y_Vcontainer[0] ,
                         self.x_Vcontainer[1] - self.x_Vcontainer[0], self.y_Vcontainer[1] - self.y_Vcontainer[0] )

        qp.end()    

    def mousePressEvent(self, event):

        #horizontal
        if self.x_Hcontainer[0] <= event.pos().x()  <= self.x_Hcontainer[1]:
            if self.y_Hcontainer[0] <= event.pos().y()  <= self.y_Hcontainer[1]:
                self.can_Hresize = True
                QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor ))
                return

        #vertical
        if self.x_Vcontainer[0] <= event.pos().x()  <= self.x_Vcontainer[1]:
            if self.y_Vcontainer[0] <= event.pos().y()  <= self.y_Vcontainer[1]:
                self.can_Vresize = True
                QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor ))
                return


    def mouseReleaseEvent(self, event):
        changed = False
        if self.can_Hresize == True :
            self.can_Hresize  = False
            changed = True

        if self.can_Vresize == True :
            self.can_Vresize  = False
            changed = True

        if changed == True :
            QtGui.QApplication.restoreOverrideCursor()


    def mouseMoveEvent(self, event):
        changed = False
        if self.can_Hresize == True:
            self.end["x"] = event.pos().x()
            changed = True
            

        if self.can_Vresize == True:
            self.start["y"] = event.pos().y()
            changed = True

        if changed == True :
            self.repaint()





def main():
    
    app = QtGui.QApplication(sys.argv)
    widget = Widget()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()