from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Font import *
import LoadingThread
from GameMain import *

class Loading(QWidget):

    def __init__(self, GameMain):
        super().__init__()
        self.initUI()
        self.setWindowTitle("Loading...")
        self.resize(1000, 500)

        # Thread
        self.thread = LoadingThread.LoadingThread(GameMain, self)
        self.thread.start()

    def initUI(self):
        mainLayout = QVBoxLayout()

        # Main Label
        MainLabelLayout = self.getMainLabelLayout()

        # Loading Status Label
        LoadingLayout = self.getLoadingStatusLabelLayout()

        mainLayout.addLayout(MainLabelLayout)
        mainLayout.addLayout(LoadingLayout)

        self.setLayout(mainLayout)

    def getMainLabelLayout(self):
        # Label
        label_font = Font("Copperplate Gothic Bold", 60)
        label = QLabel('Loading...')
        label.setFont(label_font.getFont())

        # Layout
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.setAlignment(Qt.AlignCenter)
        return layout

    def getLoadingStatusLabelLayout(self):
        # LoadingStatus Label
        self.LoadingStatus = QLabel('Game Initializing...')
        ls_font = Font("Century Schoolbook", 15)
        self.LoadingStatus.setFont(ls_font.getFont())

        # Layout
        layout = QHBoxLayout()
        layout.addWidget(self.LoadingStatus)
        layout.setAlignment(Qt.AlignCenter)
        return layout

    def setLoadingStatus(self, msg):
        self.LoadingStatus.setText(msg)
        self.LoadingStatus.repaint() # update Loading Status
        self.LoadingStatus.adjustSize() # Auto adjust Font Size to fit Label

    def __str__(self):
        return self
