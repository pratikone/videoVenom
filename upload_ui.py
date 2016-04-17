# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\upload.ui'
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

class Ui_Wizard(object):
    def setupUi(self, Wizard):
        Wizard.setObjectName(_fromUtf8("Wizard"))
        Wizard.resize(482, 369)
        self.wizardPage1 = QtGui.QWizardPage()
        self.wizardPage1.setObjectName(_fromUtf8("wizardPage1"))
        self.seedBox = QtGui.QGroupBox(self.wizardPage1)
        self.seedBox.setGeometry(QtCore.QRect(20, 10, 401, 141))
        self.seedBox.setObjectName(_fromUtf8("seedBox"))
        self.seedTagTextBox = QtGui.QLineEdit(self.seedBox)
        self.seedTagTextBox.setGeometry(QtCore.QRect(30, 80, 113, 20))
        self.seedTagTextBox.setObjectName(_fromUtf8("seedTagTextBox"))
        self.label = QtGui.QLabel(self.seedBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 211, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.seedTagBtn = QtGui.QPushButton(self.seedBox)
        self.seedTagBtn.setGeometry(QtCore.QRect(170, 80, 91, 23))
        self.seedTagBtn.setObjectName(_fromUtf8("seedTagBtn"))
        self.tagsBox = QtGui.QGroupBox(self.wizardPage1)
        self.tagsBox.setGeometry(QtCore.QRect(20, 160, 401, 111))
        self.tagsBox.setObjectName(_fromUtf8("tagsBox"))
        self.textEdit = QtGui.QTextEdit(self.tagsBox)
        self.textEdit.setGeometry(QtCore.QRect(30, 40, 351, 51))
        self.textEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label_2 = QtGui.QLabel(self.tagsBox)
        self.label_2.setGeometry(QtCore.QRect(40, 20, 251, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        Wizard.addPage(self.wizardPage1)
        self.wizardPage2 = QtGui.QWizardPage()
        self.wizardPage2.setObjectName(_fromUtf8("wizardPage2"))
        self.uploadBox = QtGui.QGroupBox(self.wizardPage2)
        self.uploadBox.setGeometry(QtCore.QRect(10, 10, 401, 311))
        self.uploadBox.setObjectName(_fromUtf8("uploadBox"))
        self.youtubeBtn = QtGui.QPushButton(self.uploadBox)
        self.youtubeBtn.setGeometry(QtCore.QRect(30, 40, 91, 61))
        self.youtubeBtn.setObjectName(_fromUtf8("youtubeBtn"))
        Wizard.addPage(self.wizardPage2)

        self.retranslateUi(Wizard)
        QtCore.QMetaObject.connectSlotsByName(Wizard)

    def retranslateUi(self, Wizard):
        Wizard.setWindowTitle(_translate("Wizard", "Publish and upload", None))
        self.seedBox.setTitle(_translate("Wizard", "Seed Tag", None))
        self.label.setText(_translate("Wizard", "Enter seed tag to generate multiple tags", None))
        self.seedTagBtn.setText(_translate("Wizard", "Generate tags", None))
        self.tagsBox.setTitle(_translate("Wizard", "Tags", None))
        self.label_2.setText(_translate("Wizard", "Comma separated tags. Enter custom tags too", None))
        self.uploadBox.setTitle(_translate("Wizard", "Uploading to video sharing sites", None))
        self.youtubeBtn.setText(_translate("Wizard", "Youtube", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Wizard = QtGui.QWizard()
    ui = Ui_Wizard()
    ui.setupUi(Wizard)
    Wizard.show()
    sys.exit(app.exec_())

