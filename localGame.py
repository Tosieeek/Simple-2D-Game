import random
import pygame
from map import Map
from player import Player
from playerAttributes import PlayerAttributes

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
heart = pygame.image.load('grafikaDoGry/heart.png')
heatLeft = pygame.image.load('grafikaDoGry/heart-left.png')
heatRight = pygame.image.load('grafikaDoGry/heart-right.png')

bullet1 = pygame.image.load('grafikaDoGry/bullet.png')
bullet2 = pygame.image.load('grafikaDoGry/bullet2.png')
mapSource = 'grafikaDoGry/map2.txt'
bullets = []
clock = pygame.time.Clock()
startY = -70
players = []
ticker = 0



def redrawGameWindow(win, winWidth, attributes):
    global ticker, hitTicker

    win.blit(bg, (0, 0))

    attributes[0].draw_attributes(win, winWidth, "left")
    attributes[1].draw_attributes(win, winWidth, "right")

    ticker += 1
    if ticker > 21:
        ticker = 0

#   !!! NIE USUWAĆ, TO DO TESTÓW!!!

    # pygame.draw.rect(win,(0,0,0),(x,y,width,height),3)
    # for i in range(len(map.listXto)):
    #     xFrom = map.listXfrom[i]
    #     yFrom = map.listYfrom[i]
    #     xTo = map.listXto[i]
    #     yTo = map.listYto[i]
    #     pygame.draw.line(win, map.color, (xFrom, yFrom), (xTo, yTo), map.size)
    #
    # if isJump == True:
    #     pygame.draw.circle(win, map.color,(700,100),30,5)

    if len(bullets) != 0:
        bulletsToRemove = []
        for b in bullets:
            b.move()
            if b.hitbox_check(players):
                bullets.remove(b)
                del b
                continue
            if b.state:
                win.blit(bullet2, (int(b.x), int(b.y)))
                if ticker % 3 == 0:
                    b.state = False
            else:
                win.blit(bullet1, (int(b.x), int(b.y)))
                if ticker % 3 == 0:
                    b.state = True

            if b.x < 0 or b.x > winWidth:
                bulletsToRemove.append(b)
                del b
        for b in bulletsToRemove:
            bullets.remove(b)

    for player in players:
        player.walkCount_check()

        if player.hit and ticker % 3 == 0:
            player.hitTicker -= 1
            continue
        elif player.hitTicker < 0:
            player.hitTicker = 5
            player.hit = False

        if player.left:
            win.blit(walkLeft[player.walkCount], (player.x, player.y))
            player.walkCount += 1
        elif player.right:
            win.blit(walkRight[player.walkCount], (player.x, player.y))
            player.walkCount += 1

        else:
            win.blit(stand, (player.x, player.y))
            player.walkCount = 0



    pygame.display.update()

def game(win,winWidth,winHeight):

    map = Map(mapSource, 4, (220, 47, 10), winWidth, winHeight)

    player1 = Player(winWidth, startY, pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN,pygame.K_o,pygame.K_p)
    player2 = Player(winWidth, startY,pygame.K_a,pygame.K_d,pygame.K_w,pygame.K_s,pygame.K_v,pygame.K_b)
    players.append(player1)
    players.append(player2)
    pa1 = PlayerAttributes(stand, heart, player1, heatLeft, heatRight)
    pa2 = PlayerAttributes(stand, heart, player2, heatLeft, heatRight)
    attributes = pa1,pa2

    run = True
    while run:

        clock.tick(24)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        for player in players:

            player.find_coordinates(map, bullets, winWidth)
            if player.lives == 0:
                run = False

        redrawGameWindow(win, winWidth, attributes)