import pygame
from pygame.event import EventType
from constants import *
import constants

def main():
    print("Starting asteroids!")
    print("Screen width: " + str(constants.SCREEN_WIDTH))
    print("Screen height: " + str(constants.SCREEN_HEIGHT))
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_HEIGHT, constants.SCREEN_HEIGHT))

    while True:
        screen.fill("black")
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

if __name__ == "__main__":
    main()
