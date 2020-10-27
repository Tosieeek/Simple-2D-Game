import pygame


class PlayerAttributes:
    def __init__(self, stand, heart, player, heartLeft, heartRight):

        self.heartWidth = int(43/1.2)
        self.heartHeight = int(36/1.2)
        self.padding = 4
        self.playerWidth = int(player.width/1.3)
        self.playerHeight = int(player.height/1.5)
        self.stand = pygame.transform.scale(stand, (self.playerWidth, self.playerHeight))
        self.heart = pygame.transform.scale(heart, (self.heartWidth, self.heartHeight))
        self.player = player
        self.heartLeft = pygame.transform.scale(heartLeft, (self.heartWidth, self.heartHeight))
        self.heartRight = pygame.transform.scale(heartRight, (self.heartWidth, self.heartHeight))

    # pygame.draw.rect(win, (0, 0, 0), (0, 0, self.player.constLives * self.heartWidth + self.player.width + 3 * self.padding, self.player.height + 2 * self.padding), 3)

    def draw_attributes(self, win, winWidth, site):

            if site == "left":

                if self.player.lives > 0:
                    win.blit(self.stand, (self.padding, self.padding))
                    for h in range(self.player.lives - 1):
                        win.blit(self.heart, (self.playerWidth + 2 * self.padding + h * self.heartWidth, self.padding))

                    if self.player.gotShoot == 1:
                        win.blit(self.heartLeft, (self.playerWidth + 2 * self.padding + (self.player.lives - 1) * self.heartWidth, self.padding))
                    else:
                        win.blit(self.heart, (self.playerWidth + 2 * self.padding + (self.player.lives - 1) * self.heartWidth, self.padding))

            elif site == "right":

                if self.player.lives > 0:
                    win.blit(self.stand, (winWidth - (self.playerWidth + self.padding), self.padding))
                    for h in range(self.player.lives - 1):
                        win.blit(self.heart, (winWidth - (self.playerWidth + 2 * self.padding + (h + 1) * self.heartWidth), self.padding))

                    if self.player.gotShoot == 1:
                        win.blit(self.heartRight, (winWidth - (self.playerWidth + 2 * self.padding + self.player.lives * self.heartWidth), self.padding))
                    else:
                        win.blit(self.heart, (winWidth - (self.playerWidth + 2 * self.padding + self.player.lives * self.heartWidth), self.padding))