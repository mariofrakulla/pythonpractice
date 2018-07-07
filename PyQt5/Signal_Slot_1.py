import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):
        self.setWindowIcon(QtGui.QIcon('icon.png'))

        self.lcd = QtWidgets.QLCDNumber()
        self.slider = QtWidgets.QSlider(Qt.Horizontal)
        self.slider.setMaximum(99)
        self.slider.setMinimum(1)
        self.slider.setTickInterval(3)
        self.slider.setTickPosition(QtWidgets.QSlider.TicksBelow)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.lcd)
        v_box.addWidget(self.slider)
        self.setLayout(v_box)

        self.slider.valueChanged.connect(self.lcd.display)

        self.show()


app = QtWidgets.QApplication(sys.argv)
wind = Window()
sys.exit(app.exec())