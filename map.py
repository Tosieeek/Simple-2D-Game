
class Map:
    def __init__(self, df, size, color, winWidth, winHeight):
        self.size = size
        self.color = color
        self.listXfrom = []
        self.listXto = []
        self.listYfrom = []
        self.listYto = []

        # adding ground as a platform
        self.listXfrom.append(0)
        self.listXto.append(winWidth)
        self.listYfrom.append(winHeight)
        self.listYto.append(winWidth)

        file = open(df)
        for line in file:
            tab = line.split(',')
            self.listXfrom.append(int(tab[0]))
            self.listYfrom.append(int(tab[1]))
            self.listXto.append(int(tab[2]))
            self.listYto.append(int(tab[3]))
        file.close()




