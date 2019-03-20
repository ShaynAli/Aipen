import pygame
from data_utils.classes import Maze, Pacman, Ghost
from pygame.locals import *
from random import randint
from classes import *

if __name__ == "__main__" or __name__ == "pacman":

    GAME = Maze()
    HERO = Pacman()
    VILLIAN = Ghost()
    VILLIAN2 = Ghost()
    pygame.init()
    GAME.scorefont = pygame.font.Font(None, 30)
    done = False
    clock = pygame.time.Clock()

    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == KEYDOWN:
                if event.key == K_q:
                    done = True
        HERO.pacPosition(GAME)
        GAME.screen.fill(GAME.BLACK)
        VILLIAN.ghostPosition(GAME)
        VILLIAN2.ghostPosition(GAME)
        move = randint(0, 3)
        GAME.countfinal = 0
        GAME.dispmaze()
        GAME.drawwalls()
        HERO.pos(GAME)
        VILLIAN.pos(GAME)
        VILLIAN2.pos(GAME)
        if HERO.checkGhost(VILLIAN) or HERO.checkGhost(VILLIAN2):
            done = True
            print
            "Final Score = " + (str)(GAME.score)
        elif GAME.countfinal == 1200:
            GAME.reset()
            HERO.resetpacman()
            VILLIAN.resetghost()
            VILLIAN2.resetghost()
            GAME.level += 1
        GAME.scoredisp()
        GAME.leveldisp()
        clock.tick(10)
        pygame.display.flip()
    pygame.quit()
