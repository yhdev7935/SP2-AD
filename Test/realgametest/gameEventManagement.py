import pygame
import copy
from options import *
from gameDraw import *
from gameFileManage import *

class Block(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = img
        self.rect = img.get_rect()

def gameKeyBoardEvent(self):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if self.test:
                return False
            else: return self.endgame()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.playerLeftMove = True
                self.beforepress = 'left'
            elif event.key == pygame.K_RIGHT:
                self.playerRightMove = True
                self.beforepress = 'right'
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.playerLeftMove = False
                self.beforepress = 'left'
                self.px+=2
            elif event.key == pygame.K_RIGHT:
                self.playerRightMove = False
                self.beforepress = 'right'
                self.px-=2
    return True

def getHitBox(self):
    hit_list = dict()
    self.player.rect.center = (self.px + 10, self.py + 10)
    self.player.mask = pygame.mask.from_surface(self.player.image)
    for key in blockList:
        hit_list[key] = pygame.sprite.spritecollide(self.player, self.block_list[key], False,
                                                    pygame.sprite.collide_mask)
    return hit_list

def moving(self):
    self.before_px = self.px
    self.before_py = self.py

    if self.playerLeftMove: self.px -= 2
    if self.playerRightMove: self.px += 2

    self.py += self.vel_y * self.speed * self.gravity
    self.speed = self.speed + 0.04 * self.gravity

    if self.speed <= 0 and self.gravity == -1:
        self.gravity = 1
        self.speed = 0

def init_moving(self):
    self.playerLeftMove = False
    self.playerRightMove = False

    self.gravity = 1
    self.speed = 0
    self.vel_y = 3

    self.px = self.init_px
    self.py = self.init_py

def checkIn(self, y, x, compare):
    return self.mapData[int(self.py + y)//SIZE][int(self.px + x)//SIZE] in compare

def gameHitEvent(self, hit_list):
    blocks = ['a', 'b']
    if hit_list['a'] != [] or hit_list['b'] != []:

        if (checkIn(self, -4, 10, blocks) or checkIn(self, -4, 0, blocks) or checkIn(self, -4, 20, blocks)) and self.gravity == -1:
            self.py = self.before_py
            self.py -= self.vel_y * (self.speed+0.12) * self.gravity
            self.gravity = 1
            self.speed = 0
        elif self.playerLeftMove and checkIn(self, 10, -5, blocks):
            self.px = self.px + 6
            if checkIn(self, 10, 10, blocks):
                self.px = self.before_px
                self.py = self.before_py
        elif self.playerRightMove and checkIn(self, 10, 25, blocks):
            self.px = self.px - 6
            if checkIn(self, 10, 10, blocks):
                self.px = self.before_px
                self.py = self.before_py

        elif (checkIn(self, 20, 10, 'b') or checkIn(self, 20, 0, 'b') or checkIn(self, 20, 20, 'b')) and self.gravity == 1:
            self.py = self.before_py
            self.py -= self.vel_y * (self.speed + 0.12) * self.gravity
            self.gravity = -1
            self.speed = 1.5
        elif (checkIn(self, 20, 10, 'a') or checkIn(self, 20, 0, 'a') or checkIn(self, 20, 20, 'a')) and self.gravity == 1:
            self.py = self.before_py
            self.py -= self.vel_y * (self.speed + 0.12) * self.gravity
            self.gravity = -1
            self.speed = 1
        elif self.beforepress=='left':
            self.px = self.px + 6
        elif self.beforepress=='right':
            self.px = self.px - 6

        else:
            self.px = self.before_px
            self.py = self.before_py

    if hit_list['c'] != [] or self.py > windows_size[1]:
        self.px = self.init_px
        self.py = self.init_py
        self.speed = 0
        self.gravity = -1
        # print('init')
        self.mapData = self.init_mapData

    if hit_list['s'] != []:
        y = int((self.py + 10) // SIZE)
        x = int((self.px + 10) // SIZE)
        if self.mapData[y][x] == 's': self.mapData[y][x] = 'd'
        existStar = False
        for currentList in self.mapData:
            if 's' in currentList:
                existStar = True
                break
        if self.test and not existStar: return 'test access'
    return True

def init_game(self, mapData, test):
    pygame.init()
    self.test = test
    windows_msg = "play 공튀기기"
    self.screen = pygame.display.set_mode(windows_size)
    pygame.display.set_caption(windows_msg)
    self.mapData = copy.deepcopy(mapData)
    makeBlock(self)
    self.init_mapData = copy.deepcopy(self.mapData)

def makeBlock(self):
    self.block_list = dict()
    for key in blockList:
        self.block_list[key] = pygame.sprite.Group()
    for y in range(windows_size[1] // SIZE):
        for x in range(windows_size[0] // SIZE):
            if self.mapData[y][x] == 'p':
                self.init_px = x * SIZE
                self.init_py = y * SIZE
                self.player = Block(image[self.mapData[y][x]].convert_alpha())
            elif self.mapData[y][x] != 'd' or self.mapData[y][x] != 'p':
                block = Block(image[self.mapData[y][x]].convert_alpha())
                block.rect.x = x * SIZE
                block.rect.y = y * SIZE
                block.mask = pygame.mask.from_surface(block.image)
                self.block_list[self.mapData[y][x]].add(block)