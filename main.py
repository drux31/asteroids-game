# asteroids_game/main.py
# this allows us to use code from
# the open-source pygame library
# throughout this file
import os
from constants import *

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame


def main():
    # pygame initialisation
    pygame.init()

    # screen setting
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()
