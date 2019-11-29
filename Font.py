from PyQt5.QtGui import *

class Font():

    def __init__(self, font, size):

        self.font = QFont()
        self.font.setFamily(font)
        self.font.setPointSize(size)

    def getFont(self):
        return self.font