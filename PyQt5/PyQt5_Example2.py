from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
import sys

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.label_one = QtWidgets.QLabel('Name: ')
        self.editLine = QtWidgets.QLineEdit()
        self.sexLabel = QtWidgets.QLabel('Sex: ')
        self.Male = QtWidgets.QRadioButton('Male')
        self.Female = QtWidgets.QRadioButton('Female')
        self.Date = QtWidgets.QLabel('Date: ')
        self.dateline = QtWidgets.QLineEdit()
        self.pb = QtWidgets.QPushButton('Process')

        h_b1 = QtWidgets.QHBoxLayout()
        h_b1.addWidget(self.label_one)
        h_b1.addWidget(self.editLine)

        h_b2 = QtWidgets.QHBoxLayout()
        h_b2.addWidget(self.sexLabel)
        h_b2.addWidget(self.Male)
        h_b2.addWidget(self.Female)

        h_b3 = QtWidgets.QHBoxLayout()
        h_b3.addWidget(self.Date)
        h_b3.addWidget(self.dateline)

        h_b4 = QtWidgets.QHBoxLayout()
        h_b4.addWidget(self.pb)

        hv = QtWidgets.QVBoxLayout()
        hv.addLayout(h_b1)
        hv.addLayout(h_b2)
        hv.addLayout(h_b3)
        hv.addLayout(h_b4)
        self.setLayout(hv)

        self.pb.clicked.connect(lambda : self.pb_call(self.Male.isChecked()))
        self.show()

    def pb_call(self, male):
        with open('textfile2.txt', 'w') as f:
            if male:
                gender = 'Male'
            else:
                gender = 'Female'
            name = self.editLine.text()
            date = self.dateline.text()
            curTxt = name + ', ' + gender +', '+date
            f.write(curTxt)


app = QtWidgets.QApplication(sys.argv)
wind = Window()
sys.exit(app.exec())