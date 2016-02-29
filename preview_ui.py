# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pratika/Documents/github/videoVenom/ui/preview.ui'
#
# Created: Mon Feb 29 18:47:21 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Preview(object):
    def setupUi(self, Preview):
        Preview.setObjectName(_fromUtf8("Preview"))
        Preview.resize(400, 300)
        self.pushButton = QtGui.QPushButton(Preview)
        self.pushButton.setGeometry(QtCore.QRect(290, 250, 85, 26))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.bgLabel = QtGui.QLabel(Preview)
        self.bgLabel.setGeometry(QtCore.QRect(20, 20, 351, 211))
        self.bgLabel.setText(_fromUtf8(""))
        self.bgLabel.setObjectName(_fromUtf8("bgLabel"))
        self.bannerLabel = QtGui.QLabel(Preview)
        self.bannerLabel.setGeometry(QtCore.QRect(190, 190, 58, 15))
        self.bannerLabel.setStyleSheet(_fromUtf8("background-color: rgba(200, 240, 240, 0)"))
        self.bannerLabel.setText(_fromUtf8(""))
        self.bannerLabel.setObjectName(_fromUtf8("bannerLabel"))
        self.bannerlImage = QtGui.QLabel(Preview)
        self.bannerlImage.setGeometry(QtCore.QRect(160, 140, 61, 21))
        self.bannerlImage.setText(_fromUtf8(""))
        self.bannerlImage.setObjectName(_fromUtf8("bannerlImage"))

        self.retranslateUi(Preview)
        QtCore.QMetaObject.connectSlotsByName(Preview)

    def retranslateUi(self, Preview):
        Preview.setWindowTitle(_translate("Preview", "Preview", None))
        self.pushButton.setText(_translate("Preview", "OK", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Preview = QtGui.QDialog()
    ui = Ui_Preview()
    ui.setupUi(Preview)
    Preview.show()
    sys.exit(app.exec_())

