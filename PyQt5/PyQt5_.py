import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):
        self.label1 = QtWidgets.QLabel('Enter Your New Password')
        self.ed1 = QtWidgets.QLineEdit()
        self.label2 = QtWidgets.QLabel('Confirm Your New Password')
        self.ed2 = QtWidgets.QLineEdit()
        self.label3 = QtWidgets.QLabel()
        self.pb = QtWidgets.QPushButton('Change Password')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.label1)
        v_box.addWidget(self.ed1)
        v_box.addWidget(self.label2)
        v_box.addWidget(self.ed2)
        v_box.addWidget(self.pb)
        v_box.addWidget(self.label3)
        self.setLayout(v_box)
        self.pb.clicked.connect(self.pb_call)
        self.show()

    def pb_call(self):

        if self.ed1.text() == self.ed2.text():
            self.label3.setText('Passwords match.')
        else:
            self.label3.setText('Passwords do not match')

app = QtWidgets.QApplication(sys.argv)
wind = Window()
sys.exit(app.exec())