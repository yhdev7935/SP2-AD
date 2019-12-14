import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

windows_size = [500, 500]
SIZE = 20

blockList = {
    'a': 'a',
    'b': 'b',
    'c': 'c',
    'd': 'd',
    's': 's',
    'p': 'p',
}

image = {char: pygame.image.load('image/%s.png' % char) for char in blockList.keys()}

def drawBackground(self):
    self.screen.fill(WHITE)

def drawLine(self, isgame=True):
    if isgame: return
    for y in range(0, windows_size[1], SIZE):
        pygame.draw.line(self.screen, BLACK, (0, y), (windows_size[0], y))
    for x in range(0, windows_size[0], SIZE):
        pygame.draw.line(self.screen, BLACK, (x, 0), (x, windows_size[1]))


def drawBlock(self, isgame=True):
    for y in range(0, windows_size[1], SIZE):
        for x in range(0, windows_size[0], SIZE):
            if self.mapData[y // SIZE][x // SIZE] == 'p' and isgame: continue
            self.screen.blit(image[self.mapData[y // SIZE][x // SIZE]], (x, y))

def drawPicture(self, isgame=True):
    drawBackground(self)
    drawLine(self, isgame)
    drawBlock(self, isgame)
    if isgame: self.screen.blit(image['p'], (self.px, self.py))

    pygame.time.Clock().tick(60)
    pygame.display.update()

