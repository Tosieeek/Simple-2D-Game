class Bullet:
    def __init__(self, x, y, site, owner):
        self.x = x
        self.y = y + 25
        self.site = site
        self.velocity = 13
        self.state = True
        self.size = 24
        self.owner = owner

    def move(self):
        if self.site == "left":
            self.x -= self.velocity
        elif self.site == "right":
            self.x += self.velocity

    def hitboxCheck(self, players):
        for player in players:
            if self.owner != player:
                if player.x + player.width > self.x + self.size/2 > player.x and player.y < self.y + self.size / 2 < player.y + player.height and player.hit is False:
                    player.hited()
                    return True

        return False



