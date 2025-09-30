# asteroids_game/main.py
# this allows us to use code from
# the open-source pygame library
# throughout this file
import os
from constants import *

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame


def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)


if __name__ == "__main__":
    main()
