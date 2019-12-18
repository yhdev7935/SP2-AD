from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from options import *
from Font import *
from GameMainButton import *
from GameMainLayout import *
from DataManagement import *
from options import *

class MapUploadConfirm:

    def __init__(self, GMain = None):
        self.GameMain = GMain

    def showMapNameDialog(self):
        while True:
            mapName, hasMapName = QInputDialog.getText(self.GameMain.MainLayout, 'Heroes of the storm', '맵 이름은 무엇으로 하시겠습니까?')
            if hasMapName:
                _, confirm = QInputDialog.getText(self.GameMain.MainLayout, 'Heroes of the storm', '맵 이름: {}, 맞습니까?'.format(mapName))
                if confirm:
                    print("Done!")
                    pass
                else:
                    pass
            else:
                break