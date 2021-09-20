import random
import pygame
from map import Map
from player import Player
from playerAttributes import PlayerAttributes
from jetpack import Jetpack
from network import Network

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

walkLeftWithJetpack = [pygame.image.load('grafikaDoGry/jetpack/wl0jetpack.png'),
                       pygame.image.load('grafikaDoGry/jetpack/wl1jetpack.png'),
                       pygame.image.load('grafikaDoGry/jetpack/wl2jetpack.png'),
                       pygame.image.load('grafikaDoGry/jetpack/wl3jetpack.png'),
                       pygame.image.load('grafikaDoGry/jetpack/wl2jetpack.png'),
                       pygame.image.load('grafikaDoGry/jetpack/wl1jetpack.png'),
                       pygame.image.load('grafikaDoGry/jetpack/wl0jetpack.png')]

walkRightWithJetpack = [pygame.image.load('grafikaDoGry/jetpack/wr0jetpack.png'),
                        pygame.image.load('grafikaDoGry/jetpack/wr1jetpack.png'),
                        pygame.image.load('grafikaDoGry/jetpack/wr2jetpack.png'),
                        pygame.image.load('grafikaDoGry/jetpack/wr3jetpack.png'),
                        pygame.image.load('grafikaDoGry/jetpack/wr2jetpack.png'),
                        pygame.image.load('grafikaDoGry/jetpack/wr1jetpack.png'),
                        pygame.image.load('grafikaDoGry/jetpack/wr0jetpack.png')]

flyLeft = pygame.image.load('grafikaDoGry/jetpack/wl1jetpackFire.png')
flyRight = pygame.image.load('grafikaDoGry/jetpack/wr1jetpackFire.png')
standJetpackFire = pygame.image.load('grafikaDoGry/jetpack/standjetpackFire.png')
standJetpack = pygame.image.load('grafikaDoGry/jetpack/standjetpack.png')
background = pygame.image.load('grafikaDoGry/background.png')
stand = pygame.image.load('grafikaDoGry/stand2.png')
heart = pygame.image.load('grafikaDoGry/heart.png')
heartLeft = pygame.image.load('grafikaDoGry/heart-left.png')
heartRight = pygame.image.load('grafikaDoGry/heart-right.png')

jetpackGraphics = pygame.transform.scale(pygame.image.load('grafikaDoGry/jetpack/jetpack.png'), (23, 44))
jetpackBar = pygame.image.load('grafikaDoGry/jetpack/jetpackBar.png')


bulletsGraphics = [pygame.image.load('grafikaDoGry/bullet.png'), pygame.image.load('grafikaDoGry/bullet2.png')]
mapSource = 'grafikaDoGry/map2.txt'
bullets = []
clock = pygame.time.Clock()
startY = -70
players = []
ticker = 0
jetpackTimer = 0
jetpacks = []
frequency = 24



def redrawGameWindow(win, winWidth, attributes, map):
    global ticker, hitTicker, jetpackTimer

    win.blit(background, (0, 0))

    attributes[0].draw_attributes(win, winWidth, "left")
    attributes[1].draw_attributes(win, winWidth, "right")

    ticker += 1
    ticker %= frequency + 1
    jetpackTimer += 1

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
        for bullet in bullets:
            bullet.move()
            if bullet.hitboxCheck(players):
                bullets.remove(bullet)
                del bullet
                continue
            if bullet.state:
                win.blit(bulletsGraphics[1], (int(bullet.x), int(bullet.y)))
                if ticker % 3 == 0:
                    bullet.state = False
            else:
                win.blit(bulletsGraphics[0], (int(bullet.x), int(bullet.y)))
                if ticker % 3 == 0:
                    bullet.state = True

            if bullet.x < 0 or bullet.x > winWidth:
                bulletsToRemove.append(bullet)
                del bullet
        for bullet in bulletsToRemove:
            bullets.remove(bullet)

    if jetpackTimer % 100 == 0:
        jet = Jetpack(map)
        jetpacks.append(jet)
        jetpackTimer = 0

    if len(jetpacks) != 0:
        jetpacksToRemove = []
        for jetpack in jetpacks:
            win.blit(jetpackGraphics, (jetpack.x, jetpack.y))
            jetpack.surge()

            if jetpack.existenceTimer > 0:
                jetpack.existenceTimer -= 1
            else:
                jetpacksToRemove.append(jetpack)

            if jetpack.hitboxCheck(players):
                jetpacksToRemove.append(jetpack)

        for jetpack in jetpacksToRemove:
            jetpacks.remove(jetpack)
            del jetpack

    for player in players:
        player.walkCount %= 7


        if player.hasJetpack:
            if player.jetpackTimer < 90:
                player.jetpackTimer += 1
            else:
                player.hasJetpack = False
                player.isFlying = False

        if player.hit and ticker % 3 == 0:
            player.hitTicker -= 1
            continue
        elif player.hitTicker < 0:
            player.hitTicker = 5
            player.hit = False
# wznosimy sie jetpackiem
        if player.isFlying and player.left:
            win.blit(flyLeft, (player.x, player.y))
        elif player.isFlying and player.right:
            win.blit(flyRight, (player.x, player.y))
        elif player.isFlying:
            win.blit(standJetpackFire, (player.x, player.y))
# spadamy z jetpackiem
        elif not player.isFlying and player.hasJetpack and player.isJump and player.left:
            win.blit(walkLeftWithJetpack[1], (player.x, player.y))
        elif not player.isFlying and player.hasJetpack and player.isJump and player.right:
            win.blit(walkRightWithJetpack[1], (player.x, player.y))
        elif not player.isFlying and player.hasJetpack and player.isJump:
            win.blit(standJetpack, (player.x, player.y))
# chodzenie z jetpackiem
        elif player.left and player.hasJetpack:
            win.blit(walkLeftWithJetpack[player.walkCount], (player.x, player.y))
            player.walkCount += 1
        elif player.right and player.hasJetpack:
            win.blit(walkRightWithJetpack[player.walkCount], (player.x, player.y))
            player.walkCount += 1
        elif player.hasJetpack:
            win.blit(standJetpack, (player.x, player.y))
            player.walkCount = 0
# chodzenie bez jetpacka
        elif player.left and not player.isFlying:
            win.blit(walkLeft[player.walkCount], (player.x, player.y))
            player.walkCount += 1
        elif player.right and not player.isFlying:
            win.blit(walkRight[player.walkCount], (player.x, player.y))
            player.walkCount += 1
        elif not player.isFlying:
            win.blit(stand, (player.x, player.y))
            player.walkCount = 0

    pygame.display.update()


def game(win, winWidth, winHeight):
    map = Map(mapSource, 4, (220, 47, 10), winWidth, winHeight)

    player1 = Player(winWidth, startY, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_o,
                     pygame.K_p)
    player2 = Player(winWidth, startY, pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_v, pygame.K_b)
    players.append(player1)
    players.append(player2)
    pa1 = PlayerAttributes(stand, heart, player1, heartLeft, heartRight, jetpackGraphics, jetpackBar)
    pa2 = PlayerAttributes(stand, heart, player2, heartLeft, heartRight, jetpackGraphics, jetpackBar)
    attributes = pa1, pa2


    run = True
    while run:

        clock.tick(frequency)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                run = False
        for player in players:

            player.find_coordinates(map, bullets, winWidth)

            if player.lives == 0:

                run = False

        redrawGameWindow(win, winWidth, attributes, map)
    clearAll()



def server_game(win, winWidth, winHeight):
    map = Map(mapSource, 4, (220, 47, 10), winWidth, winHeight)
    player1 = Player(winWidth, startY, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_o,
                     pygame.K_p)
    players.append(player1)
    pa1 = PlayerAttributes(stand, heart, player1, heartLeft, heartRight, jetpackGraphics, jetpackBar)

    n = Network()

    player2 = n.send(player1)
    players.append(player2)
    pa2 = PlayerAttributes(stand, heart, player2, heartLeft, heartRight, jetpackGraphics, jetpackBar)
    attributes = pa1, pa2

    run = True
    while run:

        clock.tick(frequency)

        player2 = n.send(player1)
        players[1] = player2

        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                run = False


        player1.find_coordinates(map, bullets, winWidth)


        redrawGameWindow(win, winWidth, attributes, map)
    clearAll()

def clearAll():
    global ticker, jetpackTimer
    players.clear()
    jetpacks.clear()
    bullets.clear()

    ticker = 0
    jetpackTimer = 0
