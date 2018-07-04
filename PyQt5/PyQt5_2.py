""" Practice PyQt 5 Pushbutton Callback Function"""
import sys
from PyQt5 import QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initWind()

    def initWind(self):
        self.pushbutton = QtWidgets.QPushButton('PUSH BUTTON A')
        self.label = QtWidgets.QLabel('I have not been clicked yet.')

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.label)
        h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.pushbutton)
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.setWindowTitle('PyQt Example II')
        self.setWindowIcon(QtGui.QIcon('icon.png'))

        self.pushbutton.clicked.connect(self.btn_click)
        self.show()

    def btn_click(self):
        self.label.setText('I was clicked.')

app = QtWidgets.QApplication(sys.argv)
wind = Window()
sys.exit(app.exec())