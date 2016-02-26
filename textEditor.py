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
        self.setWindowTitle('Editor')
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(200, 60, 200, 25)
        
        self.textEdit = QtGui.QTextEdit(self)
        self.textEdit.setGeometry(50, 60, 100, 25)

        self.textEdit.connect(self.textEdit, QtCore.SIGNAL("textChanged()"),
                    self.labelUpdate)


        self.btn = QtGui.QPushButton("Change Font",self)
        self.btn.move(20,120)
        self.btn.clicked.connect(self.font_choice)

        self.btn = QtGui.QPushButton("Change Color",self)
        self.btn.move(140,120)
        self.btn.clicked.connect(self.color_choice)


        self.show()

    def labelUpdate(self):
        self.label.setText(self.textEdit.toPlainText())

    def font_choice(self):
        font, valid = QtGui.QFontDialog.getFont()
        if valid:
            self.label.setFont(font)

    def color_choice(self):
        color = QtGui.QColorDialog.getColor()
        self.label.setStyleSheet("QLabel { color: %s}" % color.name())
            


    def paintEvent(self, e):
        
        lines = { "short" : 5, "long" : 12 }

        width  = self.end["x"] - self.start["x"]
        height = self.end["y"] - self.start["y"]




def main():
    
    app = QtGui.QApplication(sys.argv)
    widget = Widget()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()