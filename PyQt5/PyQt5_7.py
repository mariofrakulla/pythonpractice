""" Radio Button Example """

from PyQt5 import QtWidgets, QtGui
import sys

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):
        self.rb_one = QtWidgets.QRadioButton('Dogs')
        self.rb_two = QtWidgets.QRadioButton('Cats')
        self.lb = QtWidgets.QLabel()
        self.pb = QtWidgets.QPushButton('Check')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.lb)
        v_box.addWidget(self.rb_one)
        v_box.addWidget(self.rb_two)
        v_box.addWidget(self.pb)
        self.setLayout(v_box)
        self.pb.clicked.connect(lambda : self.pb_call(self.rb_one.isChecked()))
        self.show()

    def pb_call(self, rb):
        if rb:
            self.lb.setText('I guess you like dogs.')
        else:
            self.lb.setText('I guess you like cats')

app = QtWidgets.QApplication(sys.argv)
wind = Window()
sys.exit(app.exec())