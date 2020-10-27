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
        self.shift = 12

    def surge(self):
        if self.direction == "up" and self.shift > 0:
            self.y -= 1
            self.shift -= 1
        elif self.direction == "down" and self.shift > 0:
            self.y += 1
            self.shift -= 1
        else:
            if self.direction == "up":
                self.direction = "down"
                self.shift = 10
            elif self.direction == "down":
                self.direction = "up"
                self.shift = 10

