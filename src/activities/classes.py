import pygame
from pygame.locals import *
from random import randint


class Maze():

    def __init__(self):
        self.BLACK = (0, 0, 0)
        self.GOLD = (246, 253, 49)
        self.GREY = (50, 50, 50)
        self.RED = (255, 0, 0)
        self.BLUE = (20, 27, 229)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.width = 20
        self.height = 20
        self.margin = 1
        self.score = 0
        self.level = 1
        self.grid = []
        self.walls = []
        self.countfinal = 0
        self.make()
        self.size = [1200, 700]
        self.screen = pygame.display.set_mode(self.size)

    def make(self):
        for i in range(2, 4):
            for j in range(5, 14):
                self.walls.append([i, j])
        for i in range(3, 5):
            for j in range(7, 20):
                self.walls.append([j, i])
        for i in range(10, 12):
            for j in range(10, 15):
                self.walls.append([j, i])
        for i in range(17, 19):
            for j in range(0, 21):
                self.walls.append([j, i])
        for i in range(26, 28):
            for j in range(0, 13):
                self.walls.append([i, j])
        for i in range(4, 6):
            for j in range(31, 35):
                self.walls.append([j, i])
        for i in range(38, 40):
            for j in range(2, 21):
                self.walls.append([i, j])
        for i in range(29, 31):
            for j in range(18, 30):
                self.walls.append([i, j])
        for i in range(5, 7):
            for j in range(24, 30):
                self.walls.append([i, j])
        for i in range(23, 25):
            for j in range(10, 25):
                self.walls.append([j, i])

        for row in range(30):
            self.grid.append([])
            for column in range(40):
                self.grid[row].append(0)
        for wall in self.walls:
            self.grid[wall[1]][wall[0]] = 1
        return self

    def reset(self):
        self.grid = []
        self.walls = []
        self.countfinal = 0
        self.make()
        return self

    def scoredisp(self):
        scoretext = self.scorefont.render("Score: " + (str)(self.score), 1, self.RED)
        self.screen.blit(scoretext, (30, 650))

    def leveldisp(self):
        leveltext = self.scorefont.render("Level: " + (str)(self.level), 1, self.RED)
        self.screen.blit(leveltext, (600, 650))

    def dispmaze(self):
        for row in range(30):
            for column in range(40):
                color = self.GREY
                pygame.draw.rect(self.screen, color, [(self.margin + self.width) * column + self.margin,
                                                      (self.margin + self.height) * row + self.margin, self.width,
                                                      self.height])
                color = self.GOLD
                if self.grid[row][column] == 1:
                    self.countfinal = self.countfinal + 1
                else:
                    pygame.draw.rect(self.screen, color, [(self.margin + self.width) * column + self.margin + 7,
                                                          (self.margin + self.height) * row + self.margin + 7,
                                                          self.width - 14, self.height - 14])

    def drawwalls(self):
        for wall in self.walls:
            pygame.draw.rect(self.screen, self.BLUE, [(self.margin + self.width) * wall[0] + self.margin,
                                                      (self.margin + self.height) * wall[1] + self.margin, self.width,
                                                      self.height])


class Person(Maze):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def checkWall(self, x, y, W):
        if [x, y] in W:
            return True
        else:
            return False

    def moveleft(self, W):
        if self.x > 0:
            if self.checkWall(self.x - 1, self.y, W):
                self.x = self.x
            else:
                self.x = (self.x) - 1
        return self

    def moveright(self, W):
        if self.x < 39:
            if self.checkWall(self.x + 1, self.y, W):
                self.x = self.x
            else:
                self.x = (self.x) + 1
        return self

    def moveup(self, W):
        if self.y > 0:
            if self.checkWall(self.x, self.y - 1, W):
                self.y = self.y
            else:
                self.y = (self.y) - 1
        return self

    def movedown(self, W):
        if self.y < 29:
            if self.checkWall(self.x, self.y + 1, W):
                self.y = self.y
            else:
                self.y = (self.y) + 1
        return self


class Pacman(Person):

    def __init__(self):
        x = randint(0, 6)
        y = randint(0, 4)
        Person.__init__(self, x, y)

    def resetpacman(self):
        x = randint(0, 6)
        y = randint(0, 4)
        Person.__init__(self, x, y)

    def collectCoin(self, Wa):
        if Wa.grid[self.y][self.x] == 0:
            return True
        else:
            return False

    def pacleft(self, Wa):
        Person.moveleft(self, Wa.walls)
        if self.collectCoin(Wa):
            Wa.grid[self.y][self.x] = 1
            Wa.score += 1
        return self

    def pacright(self, Wa):
        Person.moveright(self, Wa.walls)
        if self.collectCoin(Wa):
            Wa.grid[self.y][self.x] = 1
            Wa.score += 1
        return self

    def pacup(self, Wa):
        Person.moveup(self, Wa.walls)
        if self.collectCoin(Wa):
            Wa.grid[self.y][self.x] = 1
            Wa.score += 1
        return self

    def pacdown(self, Wa):
        Person.movedown(self, Wa.walls)
        if self.collectCoin(Wa):
            Wa.grid[self.y][self.x] = 1
            Wa.score += 1
        return self

    def pos(self, G):
        pygame.draw.rect(G.screen, G.GREEN,
                         [(G.margin + G.width) * self.x + G.margin, (G.margin + G.height) * self.y + G.margin, G.width,
                          G.height])

    def checkGhost(self, V):
        if [self.x, self.y] == [V.x, V.y]:
            return True
        else:
            return False

    def pacPosition(self, G):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.pacleft(G)
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.pacright(G)
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            self.pacup(G)
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.pacdown(G)


class Ghost(Person):

    def __init__(self):
        x = randint(20, 27)
        y = randint(15, 22)
        Person.__init__(self, x, y)

    def resetghost(self):
        x = randint(20, 27)
        y = randint(15, 22)
        Person.__init__(self, x, y)
        return self

    def ghleft(self, Wa):
        Person.moveleft(self, Wa.walls)
        return self

    def ghright(self, Wa):
        Person.moveright(self, Wa.walls)
        return self

    def ghup(self, Wa):
        Person.moveup(self, Wa.walls)
        return self

    def ghdown(self, Wa):
        Person.movedown(self, Wa.walls)
        return self

    def pos(self, G):
        pygame.draw.rect(G.screen, G.RED,
                         [(G.margin + G.width) * self.x + G.margin, (G.margin + G.height) * self.y + G.margin, G.width,
                          G.height])

    def ghostPosition(self, G):
        move = randint(0, 3)
        if move == 0:
            self.ghleft(G)
        elif move == 1:
            self.ghright(G)
        elif move == 2:
            self.ghup(G)
        elif move == 3:
            self.ghdown(G)