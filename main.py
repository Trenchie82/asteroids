import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    play = True
    black = (0, 0, 0)
    while play == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(black)
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
