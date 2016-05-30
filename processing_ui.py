# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\processing.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.animatedDial = QtGui.QDial(Dialog)
        self.animatedDial.setGeometry(QtCore.QRect(60, 40, 281, 191))
        self.animatedDial.setObjectName(_fromUtf8("animatedDial"))
        self.loadingLabel = QtGui.QLabel(Dialog)
        self.loadingLabel.setGeometry(QtCore.QRect(150, 249, 101, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(12)
        self.loadingLabel.setFont(font)
        self.loadingLabel.setObjectName(_fromUtf8("loadingLabel"))
        self.picLabel = QtGui.QLabel(Dialog)
        self.picLabel.setGeometry(QtCore.QRect(100, 20, 211, 221))
        self.picLabel.setText(_fromUtf8(""))
        self.picLabel.setPixmap(QtGui.QPixmap(_fromUtf8(":/camera/HDRCameraApp_trans.png")))
        self.picLabel.setScaledContents(True)
        self.picLabel.setObjectName(_fromUtf8("picLabel"))
        self.picLabel.raise_()
        self.animatedDial.raise_()
        self.loadingLabel.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Video Processing", None))
        self.loadingLabel.setText(_translate("Dialog", "Processing ...", None))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

