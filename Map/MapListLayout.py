# Layout of GameMain

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from MapListButton import *
from Font import *
from FileDataManagement import *
from MapDataManagement import *
from Font import *
from gameMain import *


class MapListLayout(QWidget):

    def __init__(self, GMain = None):
        super().__init__()
        self.GameMain = GMain
        self.StatusBar = QStatusBar()
        self.initUI()
        self.setWindowTitle("Map List!")
        self.resize(900, 800)

        self.changeListViewData()

    def initUI(self):
        # Vertical Layout
        self.mainLayout = QVBoxLayout()

        ## Search Layout
        self.mainLayout.addLayout(self.getSearchLayout())

        ## ListView + Button Layout
        self.mainLayout.addLayout(self.getLVBLayout())

        ## StatusBar
        self.mainLayout.addWidget(self.StatusBar)

        self.setLayout(self.mainLayout)

    # get Search Layout
    def getSearchLayout(self):
        # Widget
        sortLabel = QLabel('Sort')
        sortLabel.setFont(Font("Bahnschrift Condensed", 16).getFont())
        self.sortComboBox = QComboBox()
        self.sortComboBox.addItems(['recent Map', 'my Map'])
        self.searchLine = QLineEdit('')
        self.searchLine.setStyleSheet("border-style: outset; \
                        border-width: 5px; \
                        border-radius: 10px; \
                        border-color: grey; \
                        min-width: 10em; \
                        padding: 6px;")
        self.searchButton = MapListButton('Search',
                                     connectLayout=self,
                                     x=100, y=35,
                                     fontsize=12)

        # Event
        self.sortComboBox.currentTextChanged.connect(self.changeListViewData) # if ComboBox Text Changed
        self.searchButton.clicked.connect(self.changeListViewData)

        # Layout
        layout = QHBoxLayout()
        layout.addWidget(sortLabel)
        layout.addWidget(self.sortComboBox)
        layout.addStretch(1)
        layout.addWidget(self.searchLine)
        layout.addWidget(self.searchButton)
        return layout

    # get ListView + Button Layout
    def getLVBLayout(self):
        # ListView
        ListViewLayout = self.getListViewLayout()

        # ButtonListLayout
        ButtonListLayout = self.getButtonListLayout()

        #LVB Layout
        layout = QHBoxLayout()
        layout.addLayout(ListViewLayout)
        layout.addLayout(ButtonListLayout)
        return layout

    def getListViewLayout(self):
        # ListView Widget
        self.ListView = QListView()
        self.ListView.setFont(Font("Bahnschrift Condensed", 12).getFont())
        self.ListView.setEditTriggers(QAbstractItemView.NoEditTriggers) # Uneditable QListView
        self.ListView.doubleClicked.connect(self.processMapRawData)

        # Page Move Layout
        PageMoveLayout = self.getPageMoveLayout()

        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.ListView)
        layout.addLayout(PageMoveLayout)
        return layout

    def getPageMoveLayout(self):
        # Widget
        self.LeftMove = MapListButton('<',
                                     connectLayout=self,
                                     x=40, y=40)
        self.Page = QLabel('1')
        PageFont = Font('Century Gothic', 13)
        self.Page.setFont(PageFont.getFont())
        self.RightMove = MapListButton('>',
                                      connectLayout=self,
                                      x=40, y=40)

        # layout
        layout = QHBoxLayout()
        layout.addStretch(1)
        layout.addWidget(self.LeftMove)
        layout.addWidget(self.Page)
        layout.addWidget(self.RightMove)
        layout.addStretch(1)
        layout.setAlignment(Qt.AlignCenter)
        return layout

    def getPage(self):
        return int(self.Page.text())

    def getButtonListLayout(self):
        # Button Widgets
        self.newButton = MapListButton('New',
                                      connectLayout=self,
                                      x=120, y=60)
        self.randomButton = MapListButton('Random',
                                          connectLayout=self,
                                          x=120, y=60)
        self.backButton = MapListButton('Back',
                                       connectLayout=self,
                                       x=120, y=60)

        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.newButton)
        layout.addWidget(self.randomButton)
        layout.addWidget(self.backButton)
        layout.setAlignment(Qt.AlignTop)
        return layout

    def getMainLayout(self):
        return self.mainLayout

    def setStatus(self, msg):
        self.StatusBar.showMessage(msg)

    def processMapRawData(self, data):
        raw_data = data.data()
        map_id = getListViewData(raw_data, mapID)
        map_data = convert_mapID_to_mapData(map_id)
        print(map_data)
        game = Game(map_data)
        game.startgame(False)


    def changeListViewData(self):
        # Server OFF
        if not getDataServerOnline():
            self.setStatus("Data Server is not WORKING!!")
            return

        mapList = getSortedMapList(self.sortComboBox.currentText())
        mapList = self.SearchFilter(mapList)
        startIndex = (self.getPage() - 1) * 5
        if startIndex > len(mapList) - 1: # OverFlow
            mapList = []
        else:
            mapList = mapList[startIndex : min(startIndex + 5, len(mapList))]
        self.ListView.setModel(convert_toModel(mapList))

    def getSearchContent(self):
        return self.searchLine.text()

    def SearchFilter(self, mapList):
        input = self.getSearchContent().replace(' ', '')
        new_mapList = []
        if len(input) == 0: return mapList
        for map in mapList:
            # playerID와 mapName에서만 비교
            compare_string = map[playerID[0]] + map[mapName[0]]
            if compare_string.find(input) != -1:
                new_mapList += [map]
        return new_mapList

    def __str__(self):
        return self.getMainLayout()


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    MLLayout = MapListLayout()
    MLLayout.show()
    sys.exit(app.exec_())

