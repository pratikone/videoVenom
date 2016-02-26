#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore
import banner_ui

DELAY = 100 * 1 #  5 seconds in milli-seconds




class Widget(QtGui.QWidget) :


    start = {"x" : 50, "y" : 100 }
    end = {"x" : 300, "y" : 300 }

    def __init__(self, ui):
        super(Widget, self).__init__()
        self.ui = ui


    def initUI(self):      
        self.ui.bannerText.connect(self.ui.bannerText, QtCore.SIGNAL("textChanged(QString)"),
                    self.labelUpdate)

        self.ui.fontBtn.clicked.connect(self.font_choice)

        self.ui.colorBtn.clicked.connect(self.color_choice)


        

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
        
        lines = { "short" : 5, "long" : 12 }

        width  = self.end["x"] - self.start["x"]
        height = self.end["y"] - self.start["y"]




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
