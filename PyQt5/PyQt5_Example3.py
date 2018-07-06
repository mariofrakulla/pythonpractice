import os
import sys
from PyQt5 import QtWidgets, QtGui

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initGui()

    def initGui(self):
        self.editTxt = QtWidgets.QTextEdit()
        self.SaveBut = QtWidgets.QPushButton('Save')
        self.OpenBu = QtWidgets.QPushButton('Open')
        self.ClearBut = QtWidgets.QPushButton('Clear')
        self.setWindowIcon(QtGui.QIcon('icon.png'))

        h_box = QtWidgets.QHBoxLayout()
        h_box.addWidget(self.editTxt)

        h_box2 = QtWidgets.QHBoxLayout()
        h_box2.addWidget(self.SaveBut)
        h_box2.addWidget(self.OpenBu)
        h_box2.addWidget(self.ClearBut)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_box)
        v_box.addLayout(h_box2)

        self.SaveBut.clicked.connect(self.Save_call)
        self.ClearBut.clicked.connect(self.Clear_call)
        self.OpenBu.clicked.connect(self.OpenBu_call)
        self.setLayout(v_box)
        self.show()

    def Clear_call(self):
        self.editTxt.clear()

    def Save_call(self):
        filename = QtWidgets.QFileDialog.getSaveFileName(self,'Save File', os.getenv('HOME'))
        with open(filename[0], 'w') as f:
            mytxt = self.editTxt.toPlainText()
            filetxt = f.write(mytxt)
    def OpenBu_call(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File',os.getenv('HOME'))
        with open(filename[0],'r') as f:
            mytxt = f.read()
            self.editTxt.setText(mytxt)


app = QtWidgets.QApplication(sys.argv)
wind = Window()
sys.exit(app.exec())