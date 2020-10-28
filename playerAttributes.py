import pygame


class PlayerAttributes:
    def __init__(self, stand, heart, player, heartLeft, heartRight, jetpackGraphic, jetpackBar):
        # parametry ikonki na górze ekranu
        self.heartWidth = int(43/1.2)
        self.heartHeight = int(36/1.2)
        self.padding = 4
        self.playerIconWidth = int(player.width / 1.3)
        self.playerIconHeight = int(player.height / 1.5)
        self.stand = pygame.transform.scale(stand, (self.playerIconWidth, self.playerIconHeight))
        self.heart = pygame.transform.scale(heart, (self.heartWidth, self.heartHeight))
        self.player = player
        self.heartLeft = pygame.transform.scale(heartLeft, (self.heartWidth, self.heartHeight))
        self.heartRight = pygame.transform.scale(heartRight, (self.heartWidth, self.heartHeight))
        self.jetpackGraphic = jetpackGraphic
        self.jetpackBar = jetpackBar
        self.jetpackWidth = 22


    def draw_attributes(self, win, winWidth, site):

            if site == "left":

                if self.player.lives > 0:
                    win.blit(self.stand, (self.padding, self.padding))
                    for h in range(self.player.lives - 1):
                        win.blit(self.heart, (self.playerIconWidth + 2 * self.padding + h * self.heartWidth, self.padding))

                    if self.player.gotShoot == 1:
                        win.blit(self.heartLeft, (self.playerIconWidth + 2 * self.padding + (self.player.lives - 1) * self.heartWidth, self.padding))
                    else:
                        win.blit(self.heart, (self.playerIconWidth + 2 * self.padding + (self.player.lives - 1) * self.heartWidth, self.padding))
                    if self.player.hasJetpack:
                        win.blit(self.jetpackGraphic, (self.padding, 2 * self.padding + self.playerIconHeight))
                        # tutaj trzeba uważać bo opieramy się na zmiennych playera przy używaniu grafiki jetpacka :(
                        win.blit(pygame.transform.scale(self.jetpackBar, (int(4*self.player.width-(self.player.jetpackTimer/90 * 4*self.player.width)), int(self.playerIconHeight/2))), (2 * self.padding + self.jetpackWidth, 2 * self.padding + self.playerIconHeight+int(self.playerIconHeight/4)))

            elif site == "right":

                if self.player.lives > 0:
                    win.blit(self.stand, (winWidth - (self.playerIconWidth + self.padding), self.padding))
                    for h in range(self.player.lives - 1):
                        win.blit(self.heart, (winWidth - (self.playerIconWidth + 2 * self.padding + (h + 1) * self.heartWidth), self.padding))

                    if self.player.gotShoot == 1:
                        win.blit(self.heartRight, (winWidth - (self.playerIconWidth + 2 * self.padding + self.player.lives * self.heartWidth), self.padding))
                    else:
                        win.blit(self.heart, (winWidth - (self.playerIconWidth + 2 * self.padding + self.player.lives * self.heartWidth), self.padding))

                    if self.player.hasJetpack:
                        win.blit(self.jetpackGraphic, (winWidth-(self.jetpackWidth+self.padding), 2 * self.padding + self.playerIconHeight))
                        # tutaj trzeba uważać bo opieramy się na zmiennych playera przy używaniu grafiki jetpacka :(
                        win.blit(pygame.transform.scale(self.jetpackBar, (int(4*self.player.width-(self.player.jetpackTimer/90 * 4*self.player.width)), int(self.playerIconHeight/2))),( winWidth - self.jetpackWidth - self.padding -int(4*self.player.width-(self.player.jetpackTimer/90 * 4*self.player.width)), 2 * self.padding + self.playerIconHeight+int(self.playerIconHeight/4)))

