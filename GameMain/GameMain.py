# Execute Game

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from options import *
from Font import *
from GameMainButton import *
from GameMainLayout import *
from DataManagement import *
from options import *
from LoadingThread import *
from MessageBox import *

class GameMain:

    def __init__(self):
        # Initialize Loading Screen
        self.loadmsg = "Loading Game..."
        load_scr = Loading(self)

        # Initialize Game
        self.loadmsg = "Loading Player Data..."
        self.playerdata = DataManagement("playerdata.dat")
        self.loadmsg = "Loading Client ID..."
        self.initClientID()
        self.loadmsg = "Loading Server Version..."
        self.serverVersion = getServerVersion()
        self.loadmsg = "Loading Main Layout..."
        self.GameMainLayout = GameMainLayout(self)
        self.MainLayout = self.GameMainLayout
        self.loadmsg = "Complete!"

        # Check Loading Screen is Off (Exception)
        if load_scr.isActiveWindow():
            load_scr.close()

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

        # Version Check
        self.showCheckVersion()

    def changetoMapList(self):
        self.quit()
        self.MainLayout = MapListLayout(self)
        self.start()

    def changetoGameMainLayout(self):
        self.quit()
        self.MainLayout = self.GameMainLayout
        self.start()

    def showCheckVersion(self):
        if VERSION != self.serverVersion and self.serverVersion != SERVER_DISCONNECTED:
            msgtext = "New Version: %s\nYOU NEED TO DOWNLOAD!" % self.serverVersion
            _msgbox = MessageBox(msgtext, "New Version AVAILABLE!", "Century Schoolbook", 20)
            _msgbox.exec_()
            return False
        return True

    def quit(self):
        self.MainLayout.close()

    def hideWindow(self):
        self.MainLayout.hide()

    def showWindow(self):
        self.MainLayout.show()

if __name__ == "__main__":

    import sys

    app = QApplication(sys.argv)
    Game = GameMain()
    Game.start()
    sys.exit(app.exec_())
