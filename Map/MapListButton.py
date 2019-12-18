from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from options import *
from Font import *
from GameMainButton import *
from MessageBox import *
from MapListLayout import *

class MapListButton(QPushButton):
    def __init__(self, text, connectLayout, x = 120, y = 60, fontname = "Bahnschrift Condensed", fontsize = 16):
        # Initialization
        super().__init__(text)
        font = Font(fontname, fontsize)
        font.setBold(True)
        self.setFont(font.getFont())
        self.setFlat(True)
        self.setStyleSheet("border-style: outset; \
                        border-width: 5px; \
                        border-radius: 10px; \
                        border-color: grey; \
                        min-width: 6em; \
                        padding: 1px;")
        self.setFixedSize(x, y)
        self.clicked.connect(self.buttonClicked)
        self.GameMain = connectLayout.GameMain
        self.connectedLayout = connectLayout

    # Equivalent with getButton Method
    def __str__(self):
        return self

    def buttonClicked(self):
        self.connectedLayout.setStatus("")
        text = self.sender().text()

        # When Search Button Clicked
        if text == "Search":
            self.onSearchClick()

        if text == "Back":
            self.onBackClick()

        # Page Move!
        if text == "<":
            self.onLeftMoveClick()

        if text == ">":
            self.onRightMoveClick()

    def onSearchClick(self):
        pass

    def onBackClick(self):
        self.GameMain.changetoGameMainLayout()

    def onLeftMoveClick(self):
        currentPage = int(self.connectedLayout.Page.text())
        self.updatePage(currentPage - 1)

    def onRightMoveClick(self):
        currentPage = int(self.connectedLayout.Page.text())
        self.updatePage(currentPage + 1)

    def updatePage(self, toPageNumber):
        if toPageNumber <= 0:
            self.connectedLayout.setStatus("Page Number can only be positive!")
        else:
            self.connectedLayout.Page.setText(str(toPageNumber))