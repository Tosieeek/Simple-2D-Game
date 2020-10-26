import pygame


class PlayerAttributes:
    def __init__(self, stand, heart, player):

        self.heartWidth = 43
        self.padding = 10
        self.stand = stand
        self.heart = heart
        self.player = player


    def draw_attributes(self, win, winWidth, site):

            if site == "left":
                pygame.draw.rect(win, (0, 0, 0), (0, 0, self.player.constLives * self.heartWidth + self.player.width + 3 * self.padding, self.player.height + 2 * self.padding), 3)
                if self.player.lives > 0:
                    for h in range(self.player.lives):
                        win.blit(self.stand, (self.padding , self.padding))
                        win.blit(self.heart, (self.player.width + 2 * self.padding + h * self.heartWidth, self.padding))
            elif site == "right":
                pygame.draw.rect(win, (0, 0, 0), (winWidth, 0, self.player.constLives * self.heartWidth + self.player.width + 3 * self.padding, self.player.height + 2 * self.padding), 3)
                if self.player.lives > 0:
                    for h in range(self.player.lives):
                        pygame.draw.rect(win, (0, 0, 0), (winWidth-(self.player.constLives * self.heartWidth + self.player.width + 3 * self.padding), 0, self.player.constLives * self.heartWidth + self.player.width + 3 * self.padding, self.player.height + 2 * self.padding), 3)
                        win.blit(self.stand, (winWidth - (self.player.width + self.padding), self.padding))
                        win.blit(self.heart, (winWidth - (self.player.width + 2 * self.padding + (h+1) * self.heartWidth), self.padding))