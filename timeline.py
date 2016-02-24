#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore

DELAY = 1000 * 1 #  5 seconds in milli-seconds


class Timeline(QtGui.QWidget):
    ctr = 0 
    def __init__(self):
        super(Timeline, self).__init__()
        
        self.initUI()
        self.timer = QtCore.QTimer(self)
        self.connect(self.timer,
                     QtCore.SIGNAL("timeout()"),
                     self.update)
        self.timer.start(DELAY)

        
    def initUI(self):      

        self.setGeometry(300, 300, 350, 100)
        self.setWindowTitle('Colours')
        self.show()

    def paintEvent(self, e):
        print "paintEvent called"
        start = {"x" : 10, "y" : 15 }
        end = {"x" : 300, "y" : 60 }
        lines = { "short" : 5, "long" : 12 }

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawRectangles(qp, start, end, lines)
        self.drawLines(qp, start, end, lines)

        self.drawTicker(qp, start, end, lines)

        qp.end()
        
    def drawRectangles(self, qp, start, end, lines):
      
        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#d4d4d4')
        qp.setPen(color)

        qp.setBrush(QtGui.QColor(255, 255, 255))
        qp.drawRect(start["x"] - 2, start["y"] - 2, end["x"], end["y"])
        
        qp.setBrush(QtGui.QColor(0, 0, 255))
        qp.drawRect(start["x"] -2  , start["y"] + lines["long"] + 3, end["x"] , start["y"] + lines["long"] + 3 + 5)

        qp.setBrush(QtGui.QColor(0, 255, 0))
        qp.drawRect(start["x"] -2 + 50  , start["y"] + lines["long"] + 3, end["x"] - 180 , start["y"] + lines["long"] + 3 + 5)
        

    def drawLines(self, qp, start, end, lines):
      
        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)

        qp.setPen(pen)
        cnt = 0
        for x in xrange( start["x"], end["x"], (end["x"] - start["x"]) / 25  ) :
            cnt = cnt + 1
            if cnt % 5 == 0:
                qp.drawLine(x, start["y"], x, start["y"] + lines["long"] )
            else :
                qp.drawLine(x, start["y"], x, start["y"] + lines["short"])
    
    def drawTicker(self, qp, start, end, lines):
      
        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(start["x"] + self.ctr, start["y"], start["x"] + self.ctr,  start["y"] + lines["long"] )
        self.ctr = self.ctr + 1



    def update( self) :
        print "something"



        self.repaint()

             

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Timeline()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()