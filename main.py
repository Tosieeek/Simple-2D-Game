import pygame
import localGame

pygame.init()
winWidth = 800
winHeight = 600
win = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("First Game")
background = pygame.image.load('grafikaDoGry/menu/menuBackground.png')
lGame = pygame.image.load('grafikaDoGry/menu/localGameButton.png')
oGame = pygame.image.load('grafikaDoGry/menu/onlineGameButton.png')
mainClock = pygame.time.Clock()

click = False
game = True
while game:
    win.blit(background, (0, 0))
    button1 = win.blit(lGame, (int((winWidth - 222)/2), 280))
    button2 = win.blit(oGame, (int((winWidth - 222) / 2), 380))
    mx, my = pygame.mouse.get_pos()


    if button1.collidepoint((mx, my)):
        if click:
            localGame.game(win, winWidth, winHeight)

    elif button2.collidepoint((mx, my)):
        if click:
            localGame.server_game(win, winWidth, winHeight)


    click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False


        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True


    mainClock.tick(24)
    pygame.display.update()





pygame.quit()
