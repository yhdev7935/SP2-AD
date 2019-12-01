from PyQt5.QtCore import *
from Loading import *
from GameMain import *
import time

class LoadingThread(QThread):

    def __init__(self, GameMain, Loading):
        super().__init__()
        self.GameMain = GameMain
        self.Loading = Loading
        self.Loading.show()

    def run(self):
        running = True
        while running:
            #print(self.GameMain.loadmsg)
            if self.GameMain.loadmsg == "Complete!":
                running = False
            self.Loading.setLoadingStatus(self.GameMain.loadmsg)
            self.msleep(1)
        self.Loading.close()



