""" Creating TextFile """
import sys
from PyQt5 import QtGui, QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):
        self.pb = QtWidgets.QPushButton('Save as .txt')
        self.txt = QtWidgets.QTextEdit()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.txt)
        v_box.addWidget(self.pb)
        self.setLayout(v_box)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.pb.clicked.connect(self.pb_call)
        self.show()

    def pb_call(self):
        with open('textfile.txt', 'w') as f:
            currentText = self.txt.toPlainText()
            f.write(currentText)

app = QtWidgets.QApplication(sys.argv)
window_one = Window()
sys.exit(app.exec())
