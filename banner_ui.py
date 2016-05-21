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
        Form.resize(794, 579)
        self.previewBtn = QtGui.QPushButton(Form)
        self.previewBtn.setGeometry(QtCore.QRect(410, 510, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setItalic(False)
        self.previewBtn.setFont(font)
        self.previewBtn.setObjectName(_fromUtf8("previewBtn"))
        self.bannerLabel = QtGui.QLabel(Form)
        self.bannerLabel.setGeometry(QtCore.QRect(210, 230, 191, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.bannerLabel.setFont(font)
        self.bannerLabel.setAutoFillBackground(False)
        self.bannerLabel.setStyleSheet(_fromUtf8("background-color: rgba(200, 240, 240, 100)"))
        self.bannerLabel.setFrameShape(QtGui.QFrame.Box)
        self.bannerLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.bannerLabel.setObjectName(_fromUtf8("bannerLabel"))
        self.frame = QtGui.QLabel(Form)
        self.frame.setGeometry(QtCore.QRect(190, 20, 541, 271))
        self.frame.setMouseTracking(False)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 100)"))
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setText(_fromUtf8(""))
        self.frame.setObjectName(_fromUtf8("frame"))
        self.progressBox = QtGui.QGroupBox(Form)
        self.progressBox.setGeometry(QtCore.QRect(20, 340, 161, 231))
        self.progressBox.setTitle(_fromUtf8(""))
        self.progressBox.setObjectName(_fromUtf8("progressBox"))
        self.nextLabel = QtGui.QLabel(self.progressBox)
        self.nextLabel.setGeometry(QtCore.QRect(10, 140, 81, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.nextLabel.setFont(font)
        self.nextLabel.setAutoFillBackground(False)
        self.nextLabel.setObjectName(_fromUtf8("nextLabel"))
        self.nextBtn = QtGui.QPushButton(self.progressBox)
        self.nextBtn.setGeometry(QtCore.QRect(10, 170, 141, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.nextBtn.setFont(font)
        self.nextBtn.setObjectName(_fromUtf8("nextBtn"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(190, 300, 531, 201))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.bannerBtn = QtGui.QPushButton(self.groupBox)
        self.bannerBtn.setGeometry(QtCore.QRect(40, 40, 471, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.bannerBtn.setFont(font)
        self.bannerBtn.setObjectName(_fromUtf8("bannerBtn"))
        self.layoutWidget = QtGui.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 85, 471, 41))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.textLabel = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.textLabel.setFont(font)
        self.textLabel.setObjectName(_fromUtf8("textLabel"))
        self.horizontalLayout.addWidget(self.textLabel)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.bannerText = QtGui.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.bannerText.setFont(font)
        self.bannerText.setObjectName(_fromUtf8("bannerText"))
        self.horizontalLayout.addWidget(self.bannerText)
        self.layoutWidget_2 = QtGui.QWidget(self.groupBox)
        self.layoutWidget_2.setGeometry(QtCore.QRect(40, 130, 471, 51))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.fontBtn = QtGui.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.fontBtn.setFont(font)
        self.fontBtn.setObjectName(_fromUtf8("fontBtn"))
        self.horizontalLayout_3.addWidget(self.fontBtn)
        self.colorBtn = QtGui.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.colorBtn.setFont(font)
        self.colorBtn.setObjectName(_fromUtf8("colorBtn"))
        self.horizontalLayout_3.addWidget(self.colorBtn)
        self.layoutWidget1 = QtGui.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.progressBox.raise_()
        self.frame.raise_()
        self.layoutWidget.raise_()
        self.previewBtn.raise_()
        self.groupBox.raise_()
        self.bannerLabel.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Set Video Banner and Text", None))
        self.previewBtn.setText(_translate("Form", "Preview ...", None))
        self.bannerLabel.setText(_translate("Form", "Banner Text", None))
        self.nextLabel.setText(_translate("Form", "Step 2/5", None))
        self.nextBtn.setText(_translate("Form", "NEXT : Set banner timeline", None))
        self.groupBox.setTitle(_translate("Form", "Banner controls", None))
        self.bannerBtn.setText(_translate("Form", "Add Banner", None))
        self.textLabel.setText(_translate("Form", "Add banner text to the video", None))
        self.bannerText.setText(_translate("Form", "Banner Text", None))
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

