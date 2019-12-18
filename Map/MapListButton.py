from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from options import *
from Font import *
from GameMainButton import *
from MessageBox import *
from MapListLayout import *
from gameMain import *
from MapDataManagement import *
import random

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

        if text == "New":
            self.onNewClick()

        if text == "Random":
            self.onRandomClick()

        if text == "Back":
            self.onBackClick()

        # Page Move!
        if text == "<":
            self.onLeftMoveClick()

        if text == ">":
            self.onRightMoveClick()

    def onNewClick(self):
        self.GameMain.hideWindow()
        game = Game()
        map_data, ok = game.startcustom()
        if ok:
            self.GameMain.MapUploadConfirm.showMapNameDialog(map_data, self.connectedLayout)
        self.GameMain.showWindow()

    def onRandomClick(self):
        mapList = getSortedMapList(self.connectedLayout.sortComboBox.currentText())
        ran_idx = random.randrange(len(mapList))
        self.connectedLayout.processMapRawData(convert_MaptoString(mapList[ran_idx]), already_rawdata = True)

    def onBackClick(self):
        self.GameMain.changetoGameMainLayout()

    def onLeftMoveClick(self):
        currentPage = int(self.connectedLayout.Page.text())
        self.updatePage(currentPage - 1)
        self.connectedLayout.changeListViewData()

    def onRightMoveClick(self):
        currentPage = int(self.connectedLayout.Page.text())
        self.updatePage(currentPage + 1)
        self.connectedLayout.changeListViewData()

    def updatePage(self, toPageNumber):
        if toPageNumber <= 0:
            self.connectedLayout.setStatus("Page Number can only be positive!")
        else:
            self.connectedLayout.Page.setText(str(toPageNumber))