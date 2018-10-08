import pygame
import math

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
        self.collide_with_deflector(state_obj.player)
        if self.pos.x + self.radius < 0 or self.pos.x - self.radius > state_obj.width or self.pos.y + self.radius < 0 or self.pos.y - self.radius > state_obj.height:
            state_obj.bullets.remove(self)
            del self
        

    #Handle collisions with the deflector
    def collide_with_deflector(self, player):
        """
        Completed with help of ryu jin from here
        https://math.stackexchange.com/questions/275529/check-if-line-intersects-with-circles-perimeter
        In this case, A is deflec_start, B is deflec_end, and C is self.pos
        """
        #First, we translate everything so that the bullet's center is at (0,0)
        deflec_start = player.deflector_start - self.pos
        deflec_end = player.deflector_end - self.pos

        a = (deflec_start.x**2) + (deflec_start.y**2) - (self.radius**2)
        b = 2*(deflec_start.x*(deflec_end.x-deflec_start.x) + deflec_start.y*(deflec_end.y-deflec_start.y))
        c = (deflec_end.x-deflec_start.x)**2 + (deflec_end.y - deflec_start.y)**2
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            return
        sqrt_discriminant = math.sqrt(discriminant)
        t1 = (-b + sqrt_discriminant)/(2*a)
        t2 = (-b - sqrt_discriminant)/(2*a)

        #The circle only intersects with the line segment when the point of intersection lies between A and B, which is when one of the values of t is between 0 and 1
        if not((0 < t1 and t1 < 1) or ( 0 < t2 and t2 < 1)):
            return





    def render(self, screen):
        pygame.draw.circle(screen, (0,0,0), self.pos.to_int().to_tuple(), self.radius)

