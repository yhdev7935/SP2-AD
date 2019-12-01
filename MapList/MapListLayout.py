# Layout of GameMain

from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MapListLayout(QWidget):

    def __init__(self, GMain = None):
        super().__init__()
        self.GameMain = GMain
        self.StatusBar = QStatusBar()
        self.initUI()
        self.setWindowTitle("Map List!")
        self.resize(1000, 500)

    def initUI(self):
        # Vertical Layout
        self.mainLayout = QVBoxLayout()

        # Search Layout
        self.mainLayout.addLayout(self.getSearchLayout())

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
        SearchButton = QPushButton('Search')

        # Event
        sortComboBox.currentTextChanged.connect(print) # if ComboBox Text Changed
        #SearchButton.clicked.connect

        # Layout
        layout = QHBoxLayout()
        layout.addWidget(sortLabel)
        layout.addWidget(sortComboBox)
        layout.addStretch(1)
        layout.addWidget(InputBox)
        layout.addWidget(SearchButton)
        return layout


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

