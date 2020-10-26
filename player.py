import random

import pygame
from bullet import Bullet

class Player:
    def __init__(self, winWidth, y, leftButton, rightButton, upButton, downButton, shotButton, flyButton):

        self.winWidth = winWidth

        self.width = 35
        self.height = 60
        self.x = random.randrange(0, self.winWidth-self.width, 1)
        self.y = y
        self.isJump = True
        self.left = False
        self.right = False
        self.vel = 6
        self.walkCount = 0
        self.actualPlatform = 0
        self.onPlatform = True
        self.platformBelowY = 0
        self.jumpCount = 8
        self.timer = 0
        self.leftButton = leftButton
        self.rightButton = rightButton
        self.upButton = upButton
        self.downButton = downButton
        self.shotButton = shotButton
        self.flyButton = flyButton
        self.lives = 3

        # just for playeAttributes class
        self.constLives = 3

        self.gotShoot = 0
        self.hit = False
        self.hitTicker = 5


    def hited(self):
        self.hit = True
        self.gotShoot += 1
        if self.gotShoot > 2:
            self.lives -= 1
            self.gotShoot = 0
            self.y = -70
            self.x = random.randrange(0, self.winWidth-self.width, 1)
            self.hit = False
            self.isJump = True




    def walkCount_check(self):
        if self.walkCount >= 7:
            self.walkCount = 0

    def belowIsPlatform(self, shift, map):
        for i in range(len(map.listXto)):
            if map.listXfrom[i] <= self.x + 2 * self.width / 3 and self.x + self.width / 3 <= map.listXto[i]:
                if self.y + self.height >= map.listYfrom[i] - map.size >= self.y + self.height - shift:
                    self.platformBelowY = map.listYfrom[i] - self.height - map.size
                    self.actualPlatform = i
                    self.onPlatform = True
                    return True
        return False

    def find_coordinates(self, map, bullets, winWidth):

        keys = pygame.key.get_pressed()

        if self.timer > 0:
            self.timer -= 1

        if keys[self.leftButton] and self.x > 0:
            self.x -= self.vel
            self.left = True
            self.right = False

            if self.x + 2 * self.width / 3 < map.listXfrom[self.actualPlatform]:
                if self.jumpCount == 8:
                    self.isJump = True
                    self.jumpCount = 0

            if keys[self.shotButton] and self.timer == 0:
                self.timer = 10
                # zrobić tak zeby bullet miał swojego playera który go rzucił
                bullet = Bullet(self.x + self.width / 2, self.y, "left", self)
                bullets.append(bullet)
        # zastanowić się żeby nie przyjmowac w metodzie winWidth
        elif keys[self.rightButton] and self.x < winWidth - self.width:
            self.x += self.vel
            self.left = False
            self.right = True

            if self.x + self.width / 3 > map.listXto[self.actualPlatform]:
                if self.jumpCount == 8:
                    self.isJump = True
                    self.jumpCount = 0

            if keys[self.shotButton] and self.timer == 0:
                self.timer = 10
                bullet = Bullet(self.x + self.width / 2, self.y, "right", self)
                bullets.append(bullet)

        else:
            self.left = False
            self.right = False
            self.walkCount = 0

        if keys[self.flyButton]:
            self.y -= 10
            self.isJump = True
            self.jumpCount = 0

        if keys[self.downButton] and self.onPlatform == True and self.y < map.listYto[0] - self.height - map.size:
            self.y = map.listYto[self.actualPlatform] - self.height + 1
            self.isJump = True
            self.jumpCount = -2

        if not self.isJump:
            if keys[self.upButton]:
                self.isJump = True
                self.walkCount = 0

        if self.isJump:
            self.onPlatform = False

            if self.jumpCount >= -8:
                shift = int((self.jumpCount * abs(self.jumpCount)) * 0.75)
                self.y -= shift
                if self.jumpCount <= 0 and self.belowIsPlatform(abs(shift), map):
                    self.y = self.platformBelowY
                    self.jumpCount = 8
                    self.isJump = False

                else:
                    self.jumpCount -= 1
            else:
                shift = int((self.jumpCount * abs(self.jumpCount)) * 0.75)
                self.y -= shift
                if self.jumpCount <= 0 and self.belowIsPlatform(abs(shift), map):
                    self.y = self.platformBelowY
                    self.jumpCount = 8
                    self.isJump = False