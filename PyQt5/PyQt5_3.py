import sys
from PyQt5 import QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initGUI()

    def initGUI(self):

        self.editLine = QtWidgets.QLineEdit()
        self.pb = QtWidgets.QPushButton('Clear')

        

        self.setWindowTitle('PyQt5 Example III')
        self.setWindowIcon(QtGui.QIcon('icon.png'))

        self.show()

app = QtWidgets.QApplication(sys.argv)
windOne = Window()
sys.exit(app.exec())