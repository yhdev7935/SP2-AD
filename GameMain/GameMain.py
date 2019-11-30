# Execute Game

from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from options import *
from Font import *
from GameMainButton import *
from GameMainLayout import *
from DataManagement import *
from options import *

class GameMain:

    def __init__(self):
        # Initialize Game
        self.playerdata = DataManagement("playerdata.dat")
        self.initClientID()

        self.MainLayout = GameMainLayout(self)
        pass

    # init Client ID
    def initClientID(self):
        KEY = CLIENT_ID_KEY
        if self.playerdata.get(KEY) is None:
            randomID = self.playerdata.genKey()
            self.playerdata.set(KEY, randomID)

    # set Status Message
    def setStatus(self, msg):
        self.MainLayout.StatusBar.showMessage(msg)

    def start(self):
        self.MainLayout.show()

    def quit(self):
        self.MainLayout.close()

if __name__ == "__main__":

    import sys

    app = QApplication(sys.argv)
    Game = GameMain()
    Game.start()
    sys.exit(app.exec_())