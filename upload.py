#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, math
from PyQt4 import QtGui, QtCore
import upload_ui


# Shows the preview window showcasing the changes made in the editor window
class Upload(QtGui.QWizard) :

    closeApp = QtCore.pyqtSignal() #signal , slot to be with caller

    def __init__(self, ui):
        super(Upload, self).__init__()
        self.ui = ui
        

    def setup_connections(self) :
        pass
        # self.ui.pushButton.clicked.connect( self.closeWidget )


    def closeEvent(self, event) :
        self.closeWidget()

    def closeWidget(self) :
        self.closeApp.emit()
        self.close()



def showUpload( caller  ) :
    ui = upload_ui.Ui_Wizard()
    widget = Upload( ui )
    ui.setupUi(widget)
    widget.setup_connections()
    widget.caller = caller
    widget.show()
    return widget



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    widget = showUpload(app)
    sys.exit(app.exec_())


     
