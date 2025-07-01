# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player 
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    print(f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0


    while True:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #replaced player.update(dt) to call the .update() method on the "updatable group" 
        #for everything in updatable:
            #everything.group.update(dt)
        
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    #shot.kill()
                    asteroid.split()  
                        

        screen.fill("black")

        #removed player.draw(screen) for the draw group
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()  
        dt = clock.tick(60) / 1000
          

if __name__ == "__main__":
    main()