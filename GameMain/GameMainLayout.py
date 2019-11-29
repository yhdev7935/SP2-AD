# Layout of GameMain

from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from options import *
from Font import *

class GameMainLayout(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Vertical Layout
        self.mainLayout = QVBoxLayout()

        ## Version Box
        self.mainLayout.addLayout(self.versionLayout())

        ## Game Name
        self.mainLayout.addWidget(self.nameWidget())

        self.setLayout(self.mainLayout)

    def versionLayout(self):
        # Initialization
        ret = QVBoxLayout()
        ClientLabel, ServerLabel = QLabel(''), QLabel('')
        ret.addWidget(ClientLabel)
        ret.addWidget(ServerLabel)
        ClientLabel.setAlignment(Qt.AlignRight)
        ServerLabel.setAlignment(Qt.AlignRight)
        vfont, vfontsize = "Century Schoolbook", 10
        clientfont, serverfont = [Font(vfont, vfontsize) for _ in [0] * 2]
        ClientLabel.setFont(clientfont.getFont())
        ServerLabel.setFont(serverfont.getFont())

        # get Client Version
        ClientVersion = VERSION # import options
        ServerVersion = "Not Connected"

        ClientLabel.setText("Client Ver: " + ClientVersion)
        ServerLabel.setText("Server Ver: " + ServerVersion)
        return ret

        # get MainLayout

    def nameWidget(self):
        # Initialization
        ret = QLabel('')
        font = Font("Copperplate Gothic Bold", 50)
        ret.setFont(font.getFont())
        ret.setAlignment(Qt.AlignBottom)
        # set Game Name
        ret.setText(GAME_TITLE)
        return ret

    def getMainLayout(self):
        return self.mainLayout

    def __str__(self):
        return self.getMainLayout()


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    GMLayout = GameMainLayout()
    GMLayout.show()
    sys.exit(app.exec_())

