import random


class Jetpack:
    def __init__(self, map):
        self.height = 29
        self.width = 15
        self.platform = random.randrange(1, len(map.listXfrom), 1)
        self.x = random.randrange(map.listXfrom[self.platform], map.listXto[self.platform], 1)
        self.startedY = map.listYfrom[self.platform] - self.height - map.size
        self.y = self.startedY
        self.direction = "up"
        self.movingTimer = 12
        self.width = 15
        self.height = 29
        self.existenceTimer = 230

    def surge(self):
        if self.direction == "up" and self.movingTimer > 0:
            self.y -= 1
            self.movingTimer -= 1
        elif self.direction == "down" and self.movingTimer > 0:
            self.y += 1
            self.movingTimer -= 1
        else:
            if self.direction == "up":
                self.direction = "down"
                self.movingTimer = 10
            elif self.direction == "down":
                self.direction = "up"
                self.movingTimer = 10

    def hitboxCheck(self, players):
        for player in players:
            if player.x + player.width > self.x + self.width / 2 > player.x and player.y < self.y + self.height / 2 < player.y + player.height:
                player.getJetpack()
                return True
        return False
