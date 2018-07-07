import sys, os
from PyQt5 import QtWidgets, QtGui

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        grid = QtWidgets.QGridLayout()
        self.lbTitle = QtWidgets.QLabel('Title: ')
        self.lbAuthor = QtWidgets.QLabel('Author: ')
        self.lbReview = QtWidgets.QLabel('Review: ')
        self.editText = QtWidgets.QLineEdit()
        self.editAuthor = QtWidgets.QLineEdit()
        self.editReview = QtWidgets.QTextEdit()
        self.addReview = QtWidgets.QPushButton('Add Review')
        self.addReview.clicked.connect(self.Review_call)

        grid.addWidget(self.lbTitle, 0, 0)
        grid.addWidget(self.editText, 0, 1, 1, 7)
        grid.addWidget(self.lbAuthor,1,0)
        grid.addWidget(self.editAuthor,1,1,1,7)
        grid.addWidget(self.lbReview, 2, 0,3,1)
        grid.addWidget(self.editReview,2,1,3,7)
        grid.addWidget(self.addReview,10,2,1,4)

        self.setLayout(grid)
        self.show()

    def Review_call(self):
        filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'))
        with open(filename[0], 'w') as f:
            Title = self.editText.text()
            Author = self.editAuthor.text()
            Review = self.editReview.toPlainText()
            myTxt = Title + ' ' + Author + ' ' + Review
            fileTxt = f.write(myTxt)


app = QtWidgets.QApplication(sys.argv)
wind = Window()
sys.exit(app.exec())