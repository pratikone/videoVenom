import sys
import basic_ui
import signals_slots
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
    
    def setup_connections( self, ui ) :
        ui.actionExit.triggered.connect(QtCore.QCoreApplication.instance().quit )

def run():
    app = QtGui.QApplication(sys.argv)
    MainWindow = Window()
    ui = basic_ui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.setup_connections(ui)
    sys.exit(app.exec_())


run()