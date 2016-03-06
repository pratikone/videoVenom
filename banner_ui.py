# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\banner.ui'
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
        Form.resize(568, 457)
        self.bannerBtn = QtGui.QPushButton(Form)
        self.bannerBtn.setGeometry(QtCore.QRect(52, 241, 491, 41))
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
        self.previewBtn = QtGui.QPushButton(Form)
        self.previewBtn.setGeometry(QtCore.QRect(340, 410, 75, 23))
        self.previewBtn.setObjectName(_fromUtf8("previewBtn"))
        self.bannerLabel = QtGui.QLabel(Form)
        self.bannerLabel.setGeometry(QtCore.QRect(110, 170, 191, 31))
        self.bannerLabel.setAutoFillBackground(False)
        self.bannerLabel.setStyleSheet(_fromUtf8("background-color: rgba(200, 240, 240, 100)"))
        self.bannerLabel.setFrameShape(QtGui.QFrame.Box)
        self.bannerLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.bannerLabel.setObjectName(_fromUtf8("bannerLabel"))
        self.frame = QtGui.QLabel(Form)
        self.frame.setGeometry(QtCore.QRect(60, 20, 481, 201))
        self.frame.setMouseTracking(False)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 100)"))
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setText(_fromUtf8(""))
        self.frame.setObjectName(_fromUtf8("frame"))
        self.okButton = QtGui.QPushButton(Form)
        self.okButton.setGeometry(QtCore.QRect(450, 410, 75, 23))
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.frame.raise_()
        self.bannerBtn.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget_2.raise_()
        self.previewBtn.raise_()
        self.bannerLabel.raise_()
        self.okButton.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Set Video Banner and Text", None))
        self.bannerBtn.setText(_translate("Form", "Add Banner", None))
        self.textLabel.setText(_translate("Form", "Add banner text to the video", None))
        self.bannerText.setText(_translate("Form", "Banner Text", None))
        self.fontBtn.setText(_translate("Form", "Select Font", None))
        self.colorBtn.setText(_translate("Form", "Set Font Color", None))
        self.previewBtn.setText(_translate("Form", "Preview ...", None))
        self.bannerLabel.setText(_translate("Form", "Banner Text", None))
        self.okButton.setText(_translate("Form", "OK", None))

