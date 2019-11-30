import pygame
from customMainDraw import *

pygame.init()

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

windows_msg = "custom 공튀기기"
screen = pygame.display.set_mode(windows_size)
pygame.display.set_caption(windows_msg)
clock = pygame.time.Clock()

mapList = [['d' for i in range(windows_size[0] // SIZE)] for j in range(windows_size[1] // SIZE)]
block = 'd'

def save():
    for y in range(windows_size[1] // SIZE):
        print(mapList[y])

while True:
    # event hook 따로 분리하지 않음
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            for char in blockList:
                if pressed[ord(char)]:
                    block = blockList[char]

            if pressed[ord('/')]: # save를 임시로 /으로 함 
                save()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            x = mouse_pos[0] // SIZE
            y = mouse_pos[1] // SIZE
            mapList[y][x] = block

    # draw UI
    drawBackground(screen)
    drawLine(screen)
    drawBlock(screen, mapList)

    clock.tick(60)
    pygame.display.update()

pygame.quit()
