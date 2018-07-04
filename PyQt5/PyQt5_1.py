from PyQt5 import QtGui
from PyQt5 import QtWidgets
import sys

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 Window'
        self.top = 100
        self.left = 200
        self.width = 650
        self.height = 500
        self.InitWindow()
        self.setWindowIcon(QtGui.QIcon("icon.png"))


    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top, self.width, self.height)

        self.l = QtWidgets.QLabel(self)
        self.l.setText('Hello World')

        self.Pb = QtWidgets.QPushButton(self)
        self.Pb.setText('Push')

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.l)
        h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.Pb)
        v_box.addLayout(h_box)

        self.setLayout(v_box)




        self.show()

App = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(App.exec())