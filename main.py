# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player 

def main():
   
    print(f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")


    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    fps = 60
    
    

    while True:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.update(dt)   
        screen.fill((0,0,0))
        player.draw(screen)
        pygame.display.flip()  
        clock.tick(fps) 
        dt = clock.tick(fps) / 1000
          

if __name__ == "__main__":
    main()