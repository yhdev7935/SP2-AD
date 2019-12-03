import pygame
from gameDraw import *
from gameFileManage import *

pygame.init()

# not same with the server yet

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

mapList = [['d' for i in range(windows_size[0] // SIZE)] for j in range(windows_size[1] // SIZE)]
mapList[1][1] = 'p'
mapList[1][3] = 's'

# example user setting
isgame = True
MapID = 'jf342ad'
MapName = 'heroes'
playerID = 'antifly55'

if isgame:
    windows_msg = "play 공튀기기"
    screen = pygame.display.set_mode(windows_size)
    pygame.display.set_caption(windows_msg)
    clock = pygame.time.Clock()

    playerLeftMove = False
    playerRightMove = False

    for y in range(windows_size[1] // SIZE):
        for x in range(windows_size[0] // SIZE):
            if mapList[y][x] == 'p':
                px = x * SIZE
                py = y * SIZE
                break

    while True:
        # event hook 따로 분리하지 않음
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerLeftMove = True
                elif event.key == pygame.K_RIGHT:
                    playerRightMove = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    playerLeftMove = False
                elif event.key == pygame.K_RIGHT:
                    playerRightMove = False

        if playerLeftMove: px -= 1
        if playerRightMove: px += 1
        # 자동으로 중력에 의해서 움직이는 것
        # 일반블럭을 밟았을때 처리
        # 점프블럭을 밟았을때 처리
        # 가시블럭을 밟았을때 처리
        # 맵을 벗어났을 때 처리
        if mapList[py // SIZE][px // SIZE] == 's':
            mapList[py // SIZE][px // SIZE] = 'd'
            for currentList in mapList:
                if 's' in currentList:
                    break

        # draw UI
        drawBackground(screen)
        drawLine(screen, isgame)
        drawBlock(screen, mapList)
        screen.blit(image['p'], (px, py))

        clock.tick(60)
        pygame.display.update()

    pygame.quit()


else:
    windows_msg = "custom 공튀기기"
    screen = pygame.display.set_mode(windows_size)
    pygame.display.set_caption(windows_msg)
    clock = pygame.time.Clock()

    block = 'd'

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
                    save(mapList)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                x = mouse_pos[0] // SIZE
                y = mouse_pos[1] // SIZE
                mapList[y][x] = block

        # draw UI
        drawBackground(screen)
        drawLine(screen, isgame)
        drawBlock(screen, mapList)

        clock.tick(60)
        pygame.display.update()

    pygame.quit()
