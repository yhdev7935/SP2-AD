from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from options import *
from Font import *
from GameMainButton import *
from MessageBox import *

class GameMainButton(QPushButton):
    def __init__(self, text, GameMain):
        # Initialization
        super().__init__(text)
        font = Font("Script MT Bold", 16)
        font.setBold(True)
        self.setFont(font.getFont())
        self.setFixedSize(120, 60)
        self.clicked.connect(self.buttonClicked)
        self.GameMain = GameMain

    # Equivalent with getButton Method
    def __str__(self):
        return self

    def buttonClicked(self):
        text = self.sender().text()

        # When Start Button Clicked
        if text == "Start":
            self.onStartClick()
            pass

        # When Map Button Clicked
        if text == "Map":
            self.onMapClick()
            pass

        # When Exit Button Clicked
        if text == "Exit":
            self.onExitClick()
            pass

    def onStartClick(self):
        pass

    def onMapClick(self):
        # Version Check
        if self.GameMain.showCheckVersion() == False:
            return

    def onExitClick(self):
        self.GameMain.quit()