from vec2 import Vec2
import pygame
import math

class Player:
    def __init__(self, x, y):

        self.pos = Vec2(x, y)
        self.vel = Vec2(0, 0)


        # Angle the deflector is facing
        self.deflector_angle = 0

        # Width of deflector
        self.deflector_width = 25
        
        #Distance the delfector is from the centre of player
        self.deflector_distance_from_player = 25

        # collisions are done using circles, so we store the radius of the player
        self.radius = 10


    # Update the player
    def update(self):
        self.pos += self.vel
        self.deflector_angle += 0.001

    def render(self, screen):
        # Draw the main player
        pygame.draw.circle(screen, (0,0,0), self.pos.to_int().to_tuple(), self.radius)


        # Find the middle of the deflector
        deflector_mid_point = self.pos + Vec2(self.deflector_distance_from_player*math.cos(self.deflector_angle),
                                              -self.deflector_distance_from_player*math.sin(self.deflector_angle))

        #Find the vector that takes you from the middle to the end of the deflector (to get to the start, just do the negative of this vector
        vec_to_end = Vec2((self.deflector_width/2)*math.sin(self.deflector_angle),
                          (self.deflector_width/2)*math.cos(self.deflector_angle))

        # Find the start and end of the deflector
        deflector_start = deflector_mid_point - vec_to_end 
        deflector_end = deflector_mid_point + vec_to_end

        # Draw the deflector
        pygame.draw.line(screen, (0,0,0), deflector_start.to_int().to_tuple(), deflector_end.to_int().to_tuple())



