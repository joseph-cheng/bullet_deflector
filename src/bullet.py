import pygame

# Bullet object that enemies will shoot, just travels linearly
class Bullet:
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel
        self.radius = 3

        #Bool of whether or not the boolean has been reflected off of the player's deflector
        self.reflected = False

    def update(self, state_obj):
        self.pos += self.vel
        if self.pos.x + self.radius < 0 or self.pos.x - self.radius > state_obj.width or self.pos.y + self.radius < 0 or self.pos.y - self.radius > state_obj.height:
            state_obj.bullets.remove(self)
            del self



    def render(self, screen):
        pygame.draw.circle(screen, (0,0,0), self.pos.to_int().to_tuple(), self.radius)

