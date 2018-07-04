import sys
from PyQt5 import QtWidgets, QtGui

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):

        self.pb_Clear = QtWidgets.QPushButton('Clear')
        self.pb_Print = QtWidgets.QPushButton('Print')
        self.edtxt = QtWidgets.QLineEdit('Text...')

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.edtxt)
        v_box.addWidget(self.pb_Clear)
        v_box.addWidget(self.pb_Print)
        self.setLayout(v_box)

        self.pb_Clear.clicked.connect(self.clear_call)
        self.pb_Print.clicked.connect(self.print_call)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.show()

    def clear_call(self):
        self.edtxt.setText(' ')

    def print_call(self):
        print(self.edtxt.text())

app = QtWidgets.QApplication(sys.argv)
wind = Window()
sys.exit(app.exec())