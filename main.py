import pygame
import localGame
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

localGame.game(win,winWidth,winHeight)

pygame.quit()
