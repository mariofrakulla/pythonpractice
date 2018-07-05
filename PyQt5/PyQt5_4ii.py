import sys
from PyQt5 import QtWidgets, QtGui

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):
        self.pb_one = QtWidgets.QPushButton('Clear')
        self.pb_two = QtWidgets.QPushButton('Print')
        self.editT = QtWidgets.QLineEdit('Edit Text')

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.editT)
        v_box.addWidget(self.pb_one)
        v_box.addWidget(self.pb_two)

        self.setLayout(v_box)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.pb_one.clicked.connect(self.pb_oneCall)
        self.pb_two.clicked.connect(self.pb_oneCall)
        self.show()

    def pb_oneCall(self):
        sender = self.sender()
        if sender.text() == 'Print':
            print(self.editT.text())
        else:
            self.editT.setText('')


app = QtWidgets.QApplication(sys.argv)
windex = Window()
sys.exit(app.exec())

