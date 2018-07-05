""" Checkbox, Pushbutton, Label"""

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):
        self.pb1 = QtWidgets.QPushButton('Check')
        self.chb = QtWidgets.QCheckBox('Do You Like Dogs? ')
        self.lb = QtWidgets.QLabel()
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.lb)
        v_box.addWidget(self.chb)
        v_box.addWidget(self.pb1)
        self.setLayout(v_box)
        self.show()

        self.pb1.clicked.connect(lambda : self.pb_call(self.chb.isChecked(), self.lb))

    def pb_call(self, chb, lb):
        if chb:
            lb.setText('Yes')
        else:
            lb.setText('No')

app = QtWidgets.QApplication(sys.argv)
wind1 = Window()
sys.exit(app.exec())