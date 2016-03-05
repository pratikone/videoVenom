#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore

DELAY = 100 * 1 #  5 seconds in milli-seconds


class Timeline:

    def drawRectangles(self, qp, start, end, lines):

        width  = end["x"] - start["x"]
        height = end["y"] - start["y"]

        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#d4d4d4')
        qp.setPen(color)

        # white
        qp.setBrush(QtGui.QColor(255, 255, 255))
        qp.drawRect(start["x"] - 2, start["y"] - 2, width, height)
        
        # blue
        qp.setBrush(QtGui.QColor(0, 0, 255))
        qp.drawRect(start["x"] -2  , start["y"] + lines["long"] + 3, width , height - lines["long"] - 3)

        # green
        qp.setBrush(QtGui.QColor(0, 255, 0))
        qp.drawRect(start["x"] -2 + 50  , start["y"] + lines["long"] + 3, width - 180 , height - lines["long"] - 3)
        

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
    
    def drawTicker(self, qp, start, end, lines, ctr):
      
        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(start["x"] - 2 +  ctr, start["y"] + lines["long"] + 3 , start["x"] - 2 + ctr,  end["y"])
        ctr = ctr + 1


class Widget(QtGui.QWidget) :

    ctr = 0
    def __init__(self, timeline):
        super(Widget, self).__init__()
        
        self.timeline = timeline
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
        start = {"x" : 10, "y" : 15 }
        end = {"x" : 300, "y" : 60 }
        lines = { "short" : 5, "long" : 12 }

        qp = QtGui.QPainter()
        qp.begin(self)
        self.timeline.drawRectangles(qp, start, end, lines)
        self.timeline.drawLines(qp, start, end, lines)

        self.timeline.drawTicker(qp, start, end, lines, self.ctr)

        qp.end()    


    def update( self) :
        self.ctr = self.ctr + 1
        self.repaint()


class AnotherTimeline(QtGui.QWidget):
  
    def __init__(self, my_range):      
        super(AnotherTimeline, self).__init__()
        
        self.initUI(my_range)
        
    def initUI(self, my_range):
        
        self.setMinimumSize(1, 30 )
        self.value = 75
        self.num = []
        self.my_range = my_range
        for x in range( my_range + 1 ) :
            if x % 60 == 0 :
                self.num.append( x )



    def setValue(self, value):

        self.value = value


    def paintEvent(self, e):
      
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()
      
      
    def drawWidget(self, qp):
      
        font = QtGui.QFont('Serif', 7, QtGui.QFont.Light)
        qp.setFont(font)

        size = self.size()
        w = 400
        h = size.height()
        # step = int(round(w / 10.0))
        magnification = w / (1.0 * self.my_range) # width per sec
        step = int(magnification * 60) #minute wise

        till = int(((w / (1.0 * self.my_range)) * self.value))
        full = int(((w / (1.0 * self.my_range)) * (self.my_range)))

        # video progress bar
        qp.setPen(QtGui.QColor(255, 255, 255))
        qp.setBrush(QtGui.QColor(255, 255, 184))
        qp.drawRect(0, 0, till, h)


        pen = QtGui.QPen(QtGui.QColor(20, 20, 20), 1, QtCore.Qt.SolidLine)
            
        qp.setPen(pen)
        qp.setBrush(QtCore.Qt.NoBrush)
        qp.drawRect(0, 0, w-1, h-1)

        j = 0
        timed = 60
        for i in range(step, w, step):
            qp.drawLine(i, 0, i, 5)
            metrics = qp.fontMetrics()
            fw = metrics.width(str(timed))
            qp.drawText(i-fw/2, h/2, str(timed))
            j = j + 1
            timed = timed + 60
            


class Communicate(QtCore.QObject):
    
    updateBW = QtCore.pyqtSignal(int)



class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        #self.initUI()
        
    def initUI(self, my_range ):      

        sld = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        sld.setFocusPolicy(QtCore.Qt.NoFocus)
        sld.setRange(0, my_range)
        sld.setValue(75)
        sld.setGeometry(30, 40, 150, 30)

        self.c = Communicate()        
        self.wid = AnotherTimeline( my_range )
        self.c.updateBW[int].connect(self.wid.setValue)
        sld.valueChanged[int].connect(self.changeValue)
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.wid)
        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        
        self.setGeometry(300, 300, 390, 210)
        self.setWindowTitle('Burning widget')
        self.show()
        
    def changeValue(self, value):
             
        self.c.updateBW.emit(value)        
        self.wid.repaint()
        
        




             

def main():
    
    app = QtGui.QApplication(sys.argv)
    #ex = Timeline()
    #widget = Widget(ex)
    ey = Example()
    ey.initUI(840)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()