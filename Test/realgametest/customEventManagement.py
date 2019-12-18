import pygame
import copy
from options import *
from gameFileManage import *

def init_custom(self, mapData):
    self.mapData = copy.deepcopy(mapData)
    windows_msg = "custom 공튀기기"
    self.screen = pygame.display.set_mode(windows_size)
    pygame.display.set_caption(windows_msg)
    self.block = 'd'

def customKeyBoardEvent(self):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return self.endgame()
        elif event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            #print(pressed)
            for char in blockList:
                if pressed[ord(char)]:
                    self.block = blockList[char]
            if pressed[ord('/')]:  # save를 임시로 /으로 함
                print('a')
                if self.startgame(self.mapData, True) == 'test access':
                    save(self.mapID, self.playerID, self.init_mapData, self.mapName)
                    self.mapData = copy.deepcopy(self.init_mapData)
                    return self.endgame()
                self.mapData = copy.deepcopy(self.init_mapData)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            x = mouse_pos[0] // SIZE
            y = mouse_pos[1] // SIZE
            self.mapData[y][x] = self.block
    return True

