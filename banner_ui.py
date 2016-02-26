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
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(-1, 9, -1, 9)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.bannerBtn = QtGui.QPushButton(self.groupBox)
        self.bannerBtn.setGeometry(QtCore.QRect(41, 241, 481, 41))
        self.bannerBtn.setObjectName(_fromUtf8("bannerBtn"))
        self.frame = QtGui.QFrame(self.groupBox)
        self.frame.setGeometry(QtCore.QRect(19, 20, 521, 201))
        self.frame.setFrameShape(QtGui.QFrame.Panel)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.buttonBox = QtGui.QDialogButtonBox(self.groupBox)
        self.buttonBox.setGeometry(QtCore.QRect(430, 390, 156, 59))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.layoutWidget = QtGui.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(41, 292, 481, 41))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.textLabel = QtGui.QLabel(self.layoutWidget)
        self.textLabel.setObjectName(_fromUtf8("textLabel"))
        self.horizontalLayout_2.addWidget(self.textLabel)
        self.bannerText = QtGui.QLineEdit(self.layoutWidget)
        self.bannerText.setObjectName(_fromUtf8("bannerText"))
        self.horizontalLayout_2.addWidget(self.bannerText)
        self.layoutWidget1 = QtGui.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 330, 481, 61))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.fontBtn = QtGui.QPushButton(self.layoutWidget1)
        self.fontBtn.setObjectName(_fromUtf8("fontBtn"))
        self.horizontalLayout_3.addWidget(self.fontBtn)
        self.colorBtn = QtGui.QPushButton(self.layoutWidget1)
        self.colorBtn.setObjectName(_fromUtf8("colorBtn"))
        self.horizontalLayout_3.addWidget(self.colorBtn)
        self.layoutWidget.raise_()
        self.bannerBtn.raise_()
        self.frame.raise_()
        self.buttonBox.raise_()
        self.layoutWidget.raise_()
        self.horizontalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Set Video Banner and Text", None))
        self.groupBox.setTitle(_translate("Form", "Banner selection", None))
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

