import random
import pygame
from map import Map
from player import Player

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
bullets = []
clock = pygame.time.Clock()
startY = -70
players = []


def redrawGameWindow(win,winWidth):

    win.blit(bg, (0, 0))

#   !!! NIE USUWAĆ, TO DO TESTÓW!!!

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
            if b.state:
                win.blit(bullet2, (int(b.x), int(b.y)))
                b.state = False
            else:
                win.blit(bullet1, (int(b.x), int(b.y)))
                b.state = True

            if b.x < 0 or b.x > winWidth:
                bullets.remove(b)
                del b


    for player in players:
        player.walkCount_check()

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

    run = True
    player1 = Player(random.randrange(0, winWidth, 1), startY)
    player2 = Player(random.randrange(0, winWidth, 1), startY)
    players.append(player1)
    players.append(player2)


    while run:

        clock.tick(21)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        for player in players:

            player.find_coordinates(map, bullets, winWidth)

        redrawGameWindow(win, winWidth)