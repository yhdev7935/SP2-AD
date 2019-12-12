# Layout of GameMain

from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from MapListButton import *
from Font import *
from DataManagement import *


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
        sortLabel = QLabel('Sort: ')
        sortComboBox = QComboBox()
        sortComboBox.addItems(['My Map', 'Recent Map'])
        InputBox = QLineEdit('')
        SearchButton = MapListButton('Search',
                                     connectLayout=self,
                                     x=100, y=35,
                                     fontname="Century Gothic",
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
        model = QStringListModel([getListViewDataFormat("A", "B", "C", "D", "E")])
        self.ListView.setModel(model)
        self.ListView.setEditTriggers(QAbstractItemView.NoEditTriggers) # Uneditable QListView
        self.ListView.doubleClicked.connect(self.GameMain.hideWindow)

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
                                     x=40, y=40,
                                     fontname="Century Gothic")
        self.Page = QLabel('1')
        PageFont = Font('Century Gothic', 13)
        self.Page.setFont(PageFont.getFont())
        self.RightMove = MapListButton('>',
                                      connectLayout=self,
                                      x=40, y=40,
                                      fontname="Century Gothic")

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
                                      x=120, y=60,
                                      fontname="Century Gothic")
        self.randomButton = MapListButton('Random',
                                          connectLayout=self,
                                          x=120, y=60,
                                          fontname="Century Gothic")
        self.backButton = MapListButton('Back',
                                       connectLayout=self,
                                       x=120, y=60,
                                       fontname="Century Gothic")

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

    def __str__(self):
        return self.getMainLayout()


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    MLLayout = MapListLayout()
    MLLayout.show()
    sys.exit(app.exec_())

