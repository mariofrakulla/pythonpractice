import sys
from PyQt5 import QtWidgets, QtGui


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):

        grid = QtWidgets.QGridLayout()



        button_names = ['Cls', 'Bck','', 'Close',
                        '7', '8', '9', '/',
                        '4', '5', '6', '*',
                        '1', '2', '3', '-',
                        '0', '.', '=', '+']
        positions = [(i,j) for i in range(5) for j in range(4)]

        for position, button_name in zip(positions, button_names):

            if button_name == '':
                continue
            button = QtWidgets.QPushButton(button_name)
            grid.addWidget(button,*position)

        self.txtDisp = QtWidgets.QLineEdit('---')
        grid.addWidget(self.txtDisp, 6,0,1,4)
        self.setLayout(grid)
        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.show()

app = QtWidgets.QApplication(sys.argv)
wind = Window()
sys.exit(app.exec())