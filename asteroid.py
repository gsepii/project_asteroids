import random
import pygame
from circleshape import CircleShape
from constants import * 

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt 
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20,50)
       
        
        v_1 = self.velocity.rotate(random_angle)
        v_2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        split_1 = Asteroid(self.position.x, self.position.y, new_radius)
        split_1.velocity = v_1 * 1.2
        split_2 = Asteroid(self.position.x, self.position.y, new_radius)
        split_2.velocity = v_2 * 1.2
