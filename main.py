import pygame
import localGame

pygame.init()
winWidth = 800
winHeight = 600
win = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("First Game")

localGame.game(win,winWidth,winHeight)

pygame.quit()
