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

def drawBackground(screen):
    screen.fill(WHITE)

def drawLine(screen):
    for y in range(0, windows_size[1], SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (windows_size[0], y))
    for x in range(0, windows_size[0], SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, windows_size[1]))


def drawBlock(screen, mapList):
    for y in range(0, windows_size[1], SIZE):
        for x in range(0, windows_size[0], SIZE):
            screen.blit(image[mapList[y // SIZE][x // SIZE]], (x, y))
            pass