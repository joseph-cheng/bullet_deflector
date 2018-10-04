from vec2 import Vec2
import pygame
import math

class Player:
    def __init__(self, x, y) 
        self.pos = Vec2(x, y)
        self.vel = Vec2(0, 0)



        # collisions are done using circles, so we store the radius of the player
        self.radius = 10


    # Update the player
    def update(self):
        self.pos += self.vel

    def render(self, screen):
        pygame.draw.circle(screen, (0,0,0), self.pos.to_tuple(), self.radius)





