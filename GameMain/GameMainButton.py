from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from options import *
from Font import *
from GameMainButton import *

def onStartClick():
    pass

def onMapClick():
    pass

def onExitClick():
    pass

class GameMainButton(QPushButton):
    def __init__(self, text):
        # Initialization
        super().__init__(text)
        font = Font("Script MT Bold", 16)
        font.setBold(True)
        self.setFont(font.getFont())
        self.setFixedSize(120, 60)
        self.clicked.connect(self.buttonClicked)

    # Equivalent with getButton Method
    def __str__(self):
        return self

    def buttonClicked(self):
        text = self.sender().text()

        # When Start Button Clicked
        if text == "Start":
            onStartClick()
            pass

        # When Map Button Clicked
        if text == "Button":
            onMapClick()
            pass

        # When Exit Button Clicked
        if text == "Exit":
            pass