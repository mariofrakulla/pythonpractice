from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt
import sys

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):
        self.lbPrice = QtWidgets.QLabel('Price')
        self.lbTax = QtWidgets.QSlider(Qt.Horizontal)
        self.lbTax.setMinimum(1)
        self.lbTax.setMaximum(47)
        self.lbTax.setTickInterval(3)
        self.lbTax.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.txtBox_one = QtWidgets.QLineEdit()
        self.txtBox_two = QtWidgets.QLabel('Interest Rate')
        self.lbthree = QtWidgets.QLabel('Total: ')
        self.lbfour = QtWidgets.QLabel('---')
        self.pb = QtWidgets.QPushButton('Calculate')

        v_box = QtWidgets.QVBoxLayout()
        h_box = QtWidgets.QHBoxLayout()
        h_boxTwo = QtWidgets.QHBoxLayout()
        h_boxFour = QtWidgets.QHBoxLayout()
        h_boxTwo.addWidget(self.lbTax)
        h_boxTwo.addStretch()
        h_boxTwo.addWidget(self.txtBox_two)

        h_box.addWidget(self.lbPrice)
        h_box.addStretch()
        h_box.addWidget(self.txtBox_one)
        h_boxThree = QtWidgets.QHBoxLayout()
        h_boxThree.addWidget(self.lbthree)
        h_boxThree.addStretch()
        h_boxThree.addWidget(self.lbfour)

        h_boxFour.addStretch()
        h_boxFour.addWidget(self.pb)
        h_boxFour.addStretch()

        v_box.addLayout(h_box)
        v_box.addLayout(h_boxTwo)
        v_box.addLayout(h_boxThree)
        v_box.addLayout(h_boxFour)
        self.setLayout(v_box)

        self.pb.clicked.connect(self.pb_call)
        self.lbTax.valueChanged.connect(self.slider_call)
        self.show()

    def pb_call(self):
        curPrice = int(self.txtBox_one.text())
        curInter = int(self.lbTax.value())
        tot = curPrice + (curInter/100)*curPrice
        self.lbfour.setText(str(tot))
    def slider_call(self):
        curInter = int(self.lbTax.value())
        self.txtBox_two.setText(str(curInter))




app = QtWidgets.QApplication(sys.argv)
wind_one = Window()
sys.exit(app.exec())
