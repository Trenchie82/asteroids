import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    play = True
    black = (0, 0, 0)
    clock = pygame.time.Clock()
    dt = 0
    ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while play == True:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
        
        ship.update(dt)
        screen.fill(black)
        ship.draw(screen)        
        pygame.display.flip()
        
        
        
    
    

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
