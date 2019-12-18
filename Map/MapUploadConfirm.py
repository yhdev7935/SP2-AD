from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from options import *
from Font import *
from GameMainButton import *
from GameMainLayout import *
from FileDataManagement import *
from MapDataManagement import *
from options import *
import datetime

class MapUploadConfirm:

    def __init__(self, GMain = None):
        self.GameMain = GMain

    def showMapNameDialog(self, map_data, connectedLayout = None):
        while True:
            map_name, hasMapName = QInputDialog.getText(self.GameMain.MainLayout, 'HOS', '맵 이름은 무엇으로 하시겠습니까?')
            if hasMapName:
                _, confirm = QInputDialog.getText(self.GameMain.MainLayout, 'HOS', '맵 이름: {}, 맞습니까?'.format(map_name))
                if confirm:
                    self.upload(map_data, map_name, connectedLayout)
                    return
                else:
                    pass
            else:
                break

    def upload(self, map_data, map_name, connectedLayout = None):
        map_id = genKey()
        player_id = self.GameMain.playerdata.get(CLIENT_ID_KEY)
        time_upload = datetime.datetime.now()
        upload_data = {mapID[0]: map_id,
                       playerID[0]: player_id,
                       TimeUpload[0]: time_upload,
                       mapData[0]: str(map_data),
                       mapName[0]: map_name}
        upload(upload_data)
        connectedLayout.changeListViewData()