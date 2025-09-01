import pygame
from constants import *
from player import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    
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
        
        for sprite in updatable:
            sprite.update(dt)
        screen.fill(black)
        for sprite in drawable:
            sprite.draw(screen)        
        pygame.display.flip()
        
if __name__ == "__main__":
    main()
