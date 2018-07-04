import sys
from PyQt5 import QtGui, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initGUI()

    def initGUI(self):

        self.editLine = QtWidgets.QLineEdit('Text Goes Here')
        self.pb = QtWidgets.QPushButton('Clear')

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.editLine)
        v_box.addWidget(self.pb)

        self.setLayout(v_box)
        self.setWindowTitle('PyQt5 Example III')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.pb.clicked.connect(self.pb_call)
        self.show()

    def pb_call(self):
        self.editLine.setText(' ')

app = QtWidgets.QApplication(sys.argv)
windOne = Window()
sys.exit(app.exec())