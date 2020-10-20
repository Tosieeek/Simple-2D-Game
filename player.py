class Player:
    def __init__(self, x, y):
        self.width = 35
        self.height = 60
        self.x = x
        self.y = y - self.height
        self.isJump = True
        self.left = False
        self.right = False
        self.vel = 6
        self.walkCount = 0
        self.actualPlatform = 0
        self.onPlatform = True
        self.platformBelowY = 0
        self.jumpCount = 8
        self.timer = 10
    def walkCount_check(self):
        if self.walkCount >= 7:
            self.walkCount = 0