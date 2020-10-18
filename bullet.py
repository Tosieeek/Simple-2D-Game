class Bullet:
    def __init__(self, x, y, site):
        self.x = x
        self.y = y + 25
        self.site = site
        self.vec = 10
        self.state = True

    def move(self):
        if self.site == "left":
            self.x -= self.vec
        elif self.site =="right":
            self.x += self.vec











