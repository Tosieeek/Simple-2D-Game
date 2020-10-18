import pygame
from bullet import Bullet
from map import Map
import random

#
# font = pygame.font.SysFont("comicsansms", 72)
# txUP = font.render('/|\\', True, (0, 128, 0))
# txRI = font.render('->', True, (0, 128, 0))
# txLF = font.render('<-', True, (0, 128, 0))
# txDW = font.render('\\|/', True, (0, 128, 0))



pygame.init()
winWidth = 800
winHeight = 600
win = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('grafikaDoGry/wr0.png'), pygame.image.load('grafikaDoGry/wr1.png'),
             pygame.image.load('grafikaDoGry/wr2.png'),
             pygame.image.load('grafikaDoGry/wr3.png'), pygame.image.load('grafikaDoGry/wr2.png'),
             pygame.image.load('grafikaDoGry/wr1.png'),
             pygame.image.load('grafikaDoGry/wr0.png')]
walkLeft = [pygame.image.load('grafikaDoGry/wl0.png'), pygame.image.load('grafikaDoGry/wl1.png'),
            pygame.image.load('grafikaDoGry/wl2.png'),
            pygame.image.load('grafikaDoGry/wl3.png'), pygame.image.load('grafikaDoGry/wl2.png'),
            pygame.image.load('grafikaDoGry/wl1.png'),
            pygame.image.load('grafikaDoGry/wl0.png')]
bg = pygame.image.load('grafikaDoGry/background.png')
char = pygame.image.load('grafikaDoGry/stand2.png')
bullet1 = pygame.image.load('grafikaDoGry/bullet.png')
bullet2 = pygame.image.load('grafikaDoGry/bullet2.png')
mapSource = 'grafikaDoGry/map2.txt'

map = Map(mapSource, 4, (220, 47, 10),winWidth,winHeight)


width = 35
height = 60
vel = 7
startY = winHeight - height - map.size
x = random.randrange(0,winWidth,1)
y = startY

clock = pygame.time.Clock()

jumpCount = 8

isJump = False
left = False
right = False


walkCount = 0
bullets = []
timer = 0
actualPlatform = 0
onPlatform = True

platformBelowY = 0


def belowIsPlatform(shift):
    global map, platformBelowY, actualPlatform, onPlatform
    for i in range(len(map.listXto)):
        if map.listXfrom[i] <= x + 2 * width / 3 and x + width / 3 <= map.listXto[i]:
            if y + height >= map.listYfrom[i] >= y + height - shift:
                platformBelowY = map.listYfrom[i] - height - map.size
                actualPlatform = i
                onPlatform = True
                return True
    return False


def redrawGameWindow():
    global walkCount, y, fall, map

    # win.fill((145, 145, 145))
    win.blit(bg,(0,0))

    # pygame.draw.rect(win,(0,0,0),(x,y,width,height),3)
    # for i in range(len(map.listXto)):
    #     xFrom = map.listXfrom[i]
    #     yFrom = map.listYfrom[i]
    #     xTo = map.listXto[i]
    #     yTo = map.listYto[i]
    #     pygame.draw.line(win, map.color, (xFrom, yFrom), (xTo, yTo), map.size)

    if walkCount >= 7:
        walkCount = 0
    if isJump == True:
        pygame.draw.circle(win, map.color,(700,100),30,5)
    if len(bullets) != 0:
        for b in bullets:
            b.move()
            if b.state == True:
                win.blit(bullet2, (b.x, b.y))
                b.state = False
            else:
                win.blit(bullet1, (b.x, b.y))
                b.state = True

            if b.x < 0 or b.x > winWidth:
                bullets.remove(b)
                del b

    if left:
        win.blit(walkLeft[walkCount], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount], (x, y))
        walkCount += 1

    else:
        win.blit(char, (x, y))
        walkCount = 0

    pygame.display.update()


run = True
while run:
    clock.tick(21)
    if timer > 0:
        timer -= 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
        left = True
        right = False
# Ksawery w przyszłości chce zamknąć to w metodę!
        temp = x + 2 * width / 3

        if temp < map.listXfrom[actualPlatform]:
            print(map.listXfrom[actualPlatform])
            print(temp)

# Ksawery w przyszłości chce zamknąć to w metodę!
            if jumpCount == 8:
                isJump = True
                jumpCount = 0


        if keys[pygame.K_z] and timer == 0:
            timer = 10
            bullet = Bullet(x, y, "left")
            bullets.append(bullet)

    elif keys[pygame.K_RIGHT] and x < winWidth - width:
        x += vel
        left = False
        right = True

# Ksawery w przyszłości chce zamknąć to w metodę!
        if x + width / 3 > map.listXto[actualPlatform]:
# Ksawery w przyszłości chce zamknąć to w metodę!

            if jumpCount == 8:
                isJump = True
                jumpCount = 0

        if keys[pygame.K_z] and timer == 0:
            timer = 10
            bullet = Bullet(x, y, "right")
            bullets.append(bullet)

    else:
        left = False
        right = False
        walkCount = 0

    if keys[pygame.K_x]:
        y -= 10
        isJump = True
        jumpCount = 0


    if keys[pygame.K_DOWN] and onPlatform == True and y < startY:
        y = map.listYto[actualPlatform] - height + 1
        isJump =True
        jumpCount = -2

    if not isJump:
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:

            isJump = True
            walkCount = 0

    if isJump:
        onPlatform = False

        if jumpCount >= -8:
# Ksawery w przyszłości chce zamknąć to w metodę!
            shift = int((jumpCount * abs(jumpCount)) * 0.75)
            y -= shift
            if jumpCount <= 0 and belowIsPlatform(abs(shift)):
                y = platformBelowY
                jumpCount = 8
                isJump = False

            else:
                jumpCount -= 1
        else:
# Ksawery w przyszłości chce zamknąć to w metodę!
            shift = int((jumpCount * abs(jumpCount)) * 0.75)
            y -= shift
            if jumpCount <= 0 and belowIsPlatform(abs(shift)):
                y = platformBelowY
                jumpCount = 8
                isJump = False
    redrawGameWindow()
pygame.quit()
