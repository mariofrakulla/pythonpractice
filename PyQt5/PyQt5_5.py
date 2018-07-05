import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initGUI()

    def initGUI(self):
        self.pb1 = QtWidgets.QPushButton('Print')
        self.pb2 = QtWidgets.QPushButton('Clear')
        self.eTxt = QtWidgets.QLineEdit('Text here...')
        self.slider_one = QtWidgets.QSlider(Qt.Horizontal)
        self.slider_one.setMinimum(1)
        self.slider_one.setMaximum(99)
        self.slider_one.setValue(23)
        self.slider_one.setTickInterval(7)
        self.slider_one.setTickPosition(QtWidgets.QSlider.TicksBelow)

        self.setWindowIcon(QtGui.QIcon('icon.png'))
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.eTxt)
        v_box.addWidget(self.pb1)
        v_box.addWidget(self.pb2)
        v_box.addWidget(self.slider_one)
        self.setLayout(v_box)
        self.pb1.clicked.connect(lambda : self.pb_call(self.pb1, 'Hello From Print'))
        self.pb2.clicked.connect(lambda : self.pb_call(self.pb2, 'Hello From Clear'))
        self.slider_one.valueChanged.connect(self.v_change)
        self.show()

    def pb_call(self, b, string):

        if b.text() == 'Print':
            print(self.eTxt.text())
        else:
            self.eTxt.setText(' ')
        print(string)

    def v_change(self):
        my_value = str(self.slider_one.value())
        self.eTxt.setText(my_value)

app = QtWidgets.QApplication(sys.argv)
window_one = Window()
sys.exit(app.exec())