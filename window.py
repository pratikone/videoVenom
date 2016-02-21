import sys
import basic_ui
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        #self.setGeometry(50, 50, 500, 300)
        #self.setWindowTitle("PyQT tuts!")
        #self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
        #self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn.resize(100,100)
        btn.move(100,100)
        self.show()

        
def run():
    app = QtGui.QApplication(sys.argv)
    MainWindow = Window()
    ui = basic_ui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

    print "yo"
    sys.exit(app.exec_())

run()