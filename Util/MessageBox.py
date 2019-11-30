from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Font import *

class MessageBox(QMessageBox):
    def __init__(self, text, windowtitle, fontname, fontsize):
        super().__init__()
        self.setText(text)
        self.setStandardButtons(QMessageBox.Ok | QMessageBox.Close)
        self.setWindowTitle(windowtitle)
        self.setFont(Font(fontname, fontsize).getFont())

    def __str__(self):
        return self