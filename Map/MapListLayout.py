# Layout of GameMain

from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from MapListButton import *
from Font import *
from DataManagement import *
from Font import *


class MapListLayout(QWidget):

    def __init__(self, GMain = None):
        super().__init__()
        self.GameMain = GMain
        self.StatusBar = QStatusBar()
        self.initUI()
        self.setWindowTitle("Map List!")
        self.resize(900, 800)

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
        sortComboBox = QComboBox()
        sortComboBox.addItems(['My Map', 'Recent Map'])
        InputBox = QLineEdit('')
        InputBox.setStyleSheet("border-style: outset; \
                        border-width: 5px; \
                        border-radius: 10px; \
                        border-color: grey; \
                        min-width: 10em; \
                        padding: 6px;")
        SearchButton = MapListButton('Search',
                                     connectLayout=self,
                                     x=100, y=35,
                                     fontsize=12)

        # Event
        sortComboBox.currentTextChanged.connect(print) # if ComboBox Text Changed

        # Layout
        layout = QHBoxLayout()
        layout.addWidget(sortLabel)
        layout.addWidget(sortComboBox)
        layout.addStretch(1)
        layout.addWidget(InputBox)
        layout.addWidget(SearchButton)
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
        lvdf = getListViewDataFormat("A", "B", "C", "D")
        model = QStringListModel([lvdf, lvdf, lvdf, lvdf, lvdf])
        self.ListView.setModel(model)
        self.ListView.setEditTriggers(QAbstractItemView.NoEditTriggers) # Uneditable QListView
        self.ListView.doubleClicked.connect(self.getMapRawData)

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

    def ListViewPrintTest(self, data):
        print(data.data())

    def getMainLayout(self):
        return self.mainLayout

    def setStatus(self, msg):
        self.StatusBar.showMessage(msg)

    def getMapRawData(self, data):
        print(data.data())

    def __str__(self):
        return self.getMainLayout()


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    MLLayout = MapListLayout()
    MLLayout.show()
    sys.exit(app.exec_())

