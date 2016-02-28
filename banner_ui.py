# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\pratika\Documents\GitHub\video venom\ui\banner.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(621, 457)
        self.bannerBtn = QtGui.QPushButton(Form)
        self.bannerBtn.setGeometry(QtCore.QRect(52, 241, 501, 41))
        self.bannerBtn.setObjectName(_fromUtf8("bannerBtn"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(52, 292, 481, 41))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.textLabel = QtGui.QLabel(self.layoutWidget)
        self.textLabel.setObjectName(_fromUtf8("textLabel"))
        self.horizontalLayout_2.addWidget(self.textLabel)
        self.bannerText = QtGui.QLineEdit(self.layoutWidget)
        self.bannerText.setObjectName(_fromUtf8("bannerText"))
        self.horizontalLayout_2.addWidget(self.bannerText)
        self.layoutWidget_2 = QtGui.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(51, 330, 481, 61))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.fontBtn = QtGui.QPushButton(self.layoutWidget_2)
        self.fontBtn.setObjectName(_fromUtf8("fontBtn"))
        self.horizontalLayout_3.addWidget(self.fontBtn)
        self.colorBtn = QtGui.QPushButton(self.layoutWidget_2)
        self.colorBtn.setObjectName(_fromUtf8("colorBtn"))
        self.horizontalLayout_3.addWidget(self.colorBtn)
        self.buttonBox = QtGui.QDialogButtonBox(Form)
        self.buttonBox.setGeometry(QtCore.QRect(441, 390, 156, 59))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(30, 20, 521, 201))
        self.frame.setFrameShape(QtGui.QFrame.Panel)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.bannerLabel = QtGui.QLabel(self.frame)
        self.bannerLabel.setGeometry(QtCore.QRect(60, 150, 141, 21))
        self.bannerLabel.setAutoFillBackground(False)
        self.bannerLabel.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0)"))
        self.bannerLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.bannerLabel.setText(_fromUtf8(""))
        self.bannerLabel.setObjectName(_fromUtf8("bannerLabel"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Set Video Banner and Text", None))
        self.bannerBtn.setText(_translate("Form", "Add Banner", None))
        self.textLabel.setText(_translate("Form", "Add banner text to the video", None))
        self.fontBtn.setText(_translate("Form", "Select Font", None))
        self.colorBtn.setText(_translate("Form", "Set Font Color", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

