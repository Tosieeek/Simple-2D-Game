import pygame
from bullet import Bullet
from map import Map
import random
from player import Player

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
stand = pygame.image.load('grafikaDoGry/stand2.png')
bullet1 = pygame.image.load('grafikaDoGry/bullet.png')
bullet2 = pygame.image.load('grafikaDoGry/bullet2.png')
mapSource = 'grafikaDoGry/map2.txt'

map = Map(mapSource, 4, (220, 47, 10),winWidth,winHeight)

# width = 35
# height = 60
# vel = 7
# x = random.randrange(0,winWidth,1)
# y = startY
# jumpCount = 8
# isJump = False
# left = False
# right = False
# walkCount = 0
# timer = 0
# actualPlatform = 0
# onPlatform = True
# platformBelowY = 0

bullets = []
clock = pygame.time.Clock()
startY = -70

def belowIsPlatform(shift, player):
    global map
    for i in range(len(map.listXto)):
        if map.listXfrom[i] <= player.x + 2 * player.width / 3 and player.x + player.width / 3 <= map.listXto[i]:
            if player.y + player.height >= map.listYfrom[i] >= player.y + player.height - shift:
                player.platformBelowY = map.listYfrom[i] - player.height - map.size
                player.actualPlatform = i
                player.onPlatform = True
                return True
    return False


def redrawGameWindow():
    global map

    win.blit(bg,(0,0))

    # pygame.draw.rect(win,(0,0,0),(x,y,width,height),3)
    # for i in range(len(map.listXto)):
    #     xFrom = map.listXfrom[i]
    #     yFrom = map.listYfrom[i]
    #     xTo = map.listXto[i]
    #     yTo = map.listYto[i]
    #     pygame.draw.line(win, map.color, (xFrom, yFrom), (xTo, yTo), map.size)

    # if isJump == True:
    #     pygame.draw.circle(win, map.color,(700,100),30,5)



    if len(bullets) != 0:
        for b in bullets:
            b.move()
            if b.state == True:
                win.blit(bullet2, (int(b.x), int(b.y)))
                b.state = False
            else:
                win.blit(bullet1, (int(b.x), int(b.y)))
                b.state = True

            if b.x < 0 or b.x > winWidth:
                bullets.remove(b)
                del b

    player1.walkCount_check()


    if player1.left:
        win.blit(walkLeft[player1.walkCount], (player1.x, player1.y))
        player1.walkCount += 1
    elif player1.right:
        win.blit(walkRight[player1.walkCount], (player1.x, player1.y))
        player1.walkCount += 1

    else:
        win.blit(stand, (player1.x, player1.y))
        player1.walkCount = 0

    pygame.display.update()


run = True

player1 = Player(random.randrange(0,winWidth,1),startY)

while run:
    clock.tick(21)

    if player1.timer > 0:
        player1.timer -= 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player1.x > 0:
        player1.x -= player1.vel
        player1.left = True
        player1.right = False



        if player1.x + 2 * player1.width / 3 < map.listXfrom[player1.actualPlatform]:
            if player1.jumpCount == 8:
                player1.isJump = True
                player1.jumpCount = 0


        if keys[pygame.K_z] and player1.timer == 0:
            player1.timer = 10
            # zrobić tak zeby bullet miał swojego playera który go rzucił
            bullet = Bullet(player1.x + player1.width/2, player1.y, "left")
            bullets.append(bullet)

    elif keys[pygame.K_RIGHT] and player1.x < winWidth - player1.width:
        player1.x += player1.vel
        player1.left = False
        player1.right = True


        if player1.x + player1.width / 3 > map.listXto[player1.actualPlatform]:
            if player1.jumpCount == 8:
                player1.isJump = True
                player1.jumpCount = 0

        if keys[pygame.K_z] and player1.timer == 0:
            player1.timer = 10
            bullet = Bullet(player1.x + player1.width/2, player1.y, "right")
            bullets.append(bullet)

    else:
        player1.left = False
        player1.right = False
        player1.walkCount = 0

    if keys[pygame.K_x]:
        player1.y -= 10
        player1.isJump = True
        player1.jumpCount = 0


    if keys[pygame.K_DOWN] and player1.onPlatform == True and player1.y < map.listYto[0] - player1.height:
        player1.y = map.listYto[player1.actualPlatform] - player1.height + 1
        player1.isJump =True
        player1.jumpCount = -2

    if not player1.isJump:
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            player1.isJump = True
            player1.walkCount = 0

    if player1.isJump:
        player1.onPlatform = False

        if player1.jumpCount >= -8:
            shift = int((player1.jumpCount * abs(player1.jumpCount)) * 0.75)
            player1.y -= shift
            if player1.jumpCount <= 0 and belowIsPlatform(abs(shift),player1):
                player1.y = player1.platformBelowY
                player1.jumpCount = 8
                player1.isJump = False

            else:
                player1.jumpCount -= 1
        else:
            shift = int((player1.jumpCount * abs(player1.jumpCount)) * 0.75)
            player1.y -= shift
            if player1.jumpCount <= 0 and belowIsPlatform(abs(shift),player1):
                player1.y = player1.platformBelowY
                player1.jumpCount = 8
                player1.isJump = False


    redrawGameWindow()
pygame.quit()
