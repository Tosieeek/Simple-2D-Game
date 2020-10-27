import pygame


class PlayerAttributes:
    def __init__(self, stand, heart, player):

        self.heartWidth = int(43/1.2)
        self.heartHeight = int(36/1.2)
        self.padding = 4
        self.playerWidth = int(player.width/1.3)
        self.playerHeight = int(player.height/1.5)
        self.stand = pygame.transform.scale(stand, (self.playerWidth, self.playerHeight))
        self.heart = pygame.transform.scale(heart, (self.heartWidth, self.heartHeight))
        self.player = player

    def draw_attributes(self, win, winWidth, site):

            if site == "left":
                # pygame.draw.rect(win, (0, 0, 0), (0, 0, self.player.constLives * self.heartWidth + self.player.width + 3 * self.padding, self.player.height + 2 * self.padding), 3)
                if self.player.lives > 0:
                    for h in range(self.player.lives):
                        win.blit(self.stand, (self.padding, self.padding))
                        win.blit(self.heart, (self.playerWidth + 2 * self.padding + h * self.heartWidth, self.padding))
            elif site == "right":
                # pygame.draw.rect(win, (0, 0, 0), (winWidth, 0, self.player.constLives * self.heartWidth + self.player.width + 3 * self.padding, self.player.height + 2 * self.padding), 3)
                if self.player.lives > 0:
                    for h in range(self.player.lives):
                        win.blit(self.stand, (winWidth - (self.playerWidth + self.padding), self.padding))
                        win.blit(self.heart, (winWidth - (self.playerWidth + 2 * self.padding + (h+1) * self.heartWidth), self.padding))