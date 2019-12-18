import pygame
from options import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

image = {char: pygame.image.load('../PyGame/image/%s.png' % char) for char in blockList.keys()}

def drawBackground(self):
    self.screen.fill(WHITE)

def drawLine(self, isgame=True):
    if isgame: return
    for y in range(0, GAME_SIZE[1], SIZE):
        pygame.draw.line(self.screen, BLACK, (0, y), (GAME_SIZE[0], y))
    for x in range(0, GAME_SIZE[0], SIZE):
        pygame.draw.line(self.screen, BLACK, (x, 0), (x, GAME_SIZE[1]))


def drawBlock(self, isgame=True):
    for y in range(0, GAME_SIZE[1], SIZE):
        for x in range(0, GAME_SIZE[0], SIZE):
            if self.mapData[y // SIZE][x // SIZE] == 'p' and isgame: continue
            elif self.mapData[y // SIZE][x // SIZE] == 'p': self.screen.blit(image['p'].subsurface(0, 0, 20, 20), (x, y))
            else: self.screen.blit(image[self.mapData[y // SIZE][x // SIZE]], (x, y))

def drawPicture(self, isgame=True):
    drawBackground(self)
    drawLine(self, isgame)
    drawBlock(self, isgame)

    if self.ptime == 10: self.ptime = 0
    self.ptime += 1

    if isgame:
        recentimg = image['p'].subsurface((20*self.ptime, 0, 20, 20))
        self.screen.blit(recentimg, (self.px, self.py))

    pygame.time.Clock().tick(60 * GAME_SPEED)
    pygame.display.update()

