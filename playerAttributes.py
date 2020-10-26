import pygame


class PlayerAttributes:
    def __init__(self, stand, heart, player):

        self.heartWidth = 43
        self.heartHeight = 36
        self.padding = 4
        self.stand = pygame.transform.scale(stand, (int(player.width/1.3), int(player.height/1.5)))
        self.heart = pygame.transform.scale(heart, (int(self.heartWidth/1.2), int(self.heartHeight/1.2)))
        self.player = player

    def draw_attributes(self, win, winWidth, site):

            if site == "left":
                #pygame.draw.rect(win, (0, 0, 0), (0, 0, self.player.constLives * self.heartWidth + self.player.width + 3 * self.padding, self.player.height + 2 * self.padding), 3)
                if self.player.lives > 0:
                    for h in range(self.player.lives):
                        win.blit(self.stand, (self.padding, self.padding))
                        win.blit(self.heart, (self.player.width + 2 * self.padding + h * self.heartWidth, self.padding))
            elif site == "right":
                #pygame.draw.rect(win, (0, 0, 0), (winWidth, 0, self.player.constLives * self.heartWidth + self.player.width + 3 * self.padding, self.player.height + 2 * self.padding), 3)
                if self.player.lives > 0:
                    for h in range(self.player.lives):
                        win.blit(self.stand, (winWidth - (self.player.width + self.padding), self.padding))
                        win.blit(self.heart, (winWidth - (self.player.width + 2 * self.padding + (h+1) * self.heartWidth), self.padding))