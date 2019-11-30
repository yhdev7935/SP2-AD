# Layout of GameMain

from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from options import *
from Font import *
from GameMainButton import *
from DataManagement import *
from Internet import *

class GameMainLayout(QWidget):

    def __init__(self, GameMain):
        super().__init__()
        self.GameMain = GameMain
        self.StatusBar = QStatusBar()
        self.initUI()
        self.setWindowTitle(GAME_TITLE)
        self.resize(1000, 500)

    def initUI(self):
        # Vertical Layout
        self.mainLayout = QVBoxLayout()

        ## Client Data Layout
        self.mainLayout.addLayout(self.ClientDataLayout())

        ## Game Name
        self.mainLayout.addWidget(self.nameWidget())

        ## Button
        self.StartButton = self.makeButtonWidget("Start")
        self.MapButton = self.makeButtonWidget("Map")
        self.ExitButton = self.makeButtonWidget("Exit")
        self.mainLayout.addLayout(self.makeButtonLayout(self.StartButton))
        if InternetConnected() == True:
            self.mainLayout.addLayout(self.makeButtonLayout(self.MapButton))
        else:
            self.setStatus("Map Button Load Failed: 인터넷이 연결이 안되어 있습니다.")
        self.mainLayout.addLayout(self.makeButtonLayout(self.ExitButton))

        ## StatusBar
        self.mainLayout.addWidget(self.StatusBar)

        self.setLayout(self.mainLayout)

    def ClientDataLayout(self):
        # Initialization
        ret = QVBoxLayout()
        Label = QLabel('')
        ret.addWidget(Label)
        Label.setAlignment(Qt.AlignRight)
        font = Font("Century Schoolbook", 10)
        Label.setFont(font.getFont())

        # get Client, Server Version
        ClientVersion = str(VERSION) # import options
        ServerVersion = str(self.GameMain.serverVersion)

        # get Client ID
        data = DataManagement("playerdata.dat")
        ClientID = data.get(CLIENT_ID_KEY)

        # Label Text
        LabelText = "Client Ver: %s\n Server Ver: %s\n Client ID: %s"\
                    % (ClientVersion, ServerVersion, ClientID)

        Label.setText(LabelText)
        return ret

        # get MainLayout

    def nameWidget(self):
        # Initialization
        ret = QLabel('')
        font = Font("Copperplate Gothic Bold", 50)
        ret.setFont(font.getFont())
        ret.setAlignment(Qt.AlignCenter)

        # set Game Name
        ret.setText(GAME_TITLE)
        ret.setToolTip("<html><head/><body><p>별을 찾아...</p></body></html>")
        return ret

    def makeButtonWidget(self, text):
        button = GameMainButton(text, self.GameMain)
        return button

    def makeButtonLayout(self, button):
        # Initialization
        layout = QHBoxLayout()
        layout.addWidget(button)
        layout.setAlignment(Qt.AlignCenter)
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
    GMLayout = GameMainLayout()
    GMLayout.show()
    sys.exit(app.exec_())

