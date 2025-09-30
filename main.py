# asteroids_game/main.py
# this allows us to use code from
# the open-source pygame library
# throughout this file
import os
from constants import *
from player import *
from asteroid import *
from asteroidfield import *


os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame


def main():
    # pygame initialisation
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    # groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables,)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    # screen setting
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for elt in drawables:
            elt.draw(screen)
        # updatable.draw(dt)

        pygame.display.flip()
        res = clock.tick(60)
        dt = res / 1000

        updatables.update(dt)


if __name__ == "__main__":
    main()
