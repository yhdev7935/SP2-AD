import pygame

pygame.init()

# 화면설계
windows_size = [300, 400]
windows_msg = "hello 공튀기기"
screen = pygame.display.set_mode(windows_size)
pygame.display.set_caption(windows_msg)

clock = pygame.time.Clock()
# 색상표현
WHITE = [255, 255, 255]
RED = [255, 0, 0]
# 게임루프
x1 = 100;
y1 = 10;
a1 = 30;
b1 = 30
gravity = 1
speed = 1
vel_y = 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (int(x1), int(y1)), 2, 1)
    #pygame.draw.rect(screen, RED, (x1, y1, a1, b1), 0)

    y1 += vel_y * speed * gravity
    speed = speed + 0.02 * gravity

    if speed < 0 and gravity == -1:
        gravity = 1
        speed = 0

    if y1 > 300 and gravity == 1:
        gravity = -1
        speed = 1

    clock.tick(60)
    pygame.display.update()

pygame.quit()



