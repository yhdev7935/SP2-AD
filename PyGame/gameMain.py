import pygame
import copy
import sys
from block import *
from options import *
from gameDraw import *
from gameFileManage import *
from gameEventManagement import *
from customEventManagement import *

class Game:
    def __init__(self, mapData=None):
        pygame.init()
        if mapData == None:
            mapData = [['d' for i in range(GAME_SIZE[0] // SIZE)] for j in range(GAME_SIZE[1] // SIZE)]
        self.mapData = mapData
        self.ptime = 0

    def startgame(self, test=False):
        init_game(self, self.mapData, test)
        init_moving(self)

        while True:
            ok = gameKeyBoardEvent(self)
            if not ok: break
            hit_list = getHitBox(self)
            moving(self)
            ok = gameHitEvent(self, hit_list)
            if ok == 'test access': return 'test access'
            elif ok == False: return
            drawPicture(self, True)

    def startcustom(self):
        init_custom(self, self.mapData)
        while True:
            ok = customKeyBoardEvent(self)
            if ok == False: break
            drawPicture(self, False)
        return self.mapData, self.testok

    def endgame(self):
        pygame.quit()
        return False

if __name__ == '__main__':
    mapID = 'yongha'
    playerID = 'hyeongbin'
    mapName = 'thisis'

    mapList = [['d' for i in range(GAME_SIZE[0] // SIZE)] for j in range(GAME_SIZE[1] // SIZE)]
    mapList[1][1] = 'p'
    mapList[1][3] = 's'
    mapList[5][1] = 'b'
    mapList[5][2] = 'a'
    mapList[5][3] = 'a'
    mapList[5][4] = 'a'
    mapList[5][5] = 'b'

    g = Game(mapList)
    #g.startgame(mapList)
    g.startcustom()