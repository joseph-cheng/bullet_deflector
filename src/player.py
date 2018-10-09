from vec2 import Vec2
import pygame
import math
import constants

class Player:
    def __init__(self, x, y):

        self.pos = Vec2(x, y)
        self.vel = Vec2(0, 0)
        self.accel = Vec2(0,0)
        self.mass = 0.02
        self.force_applied = 10
        self.friction = 0.25
        


        # Angle the deflector is facing
        self.deflector_angle = 0

        # Width of deflector
        self.deflector_width = 25
        
        #Distance the delfector is from the centre of player
        self.deflector_distance_from_player = 25

        # collisions are done using circles, so we store the radius of the player
        self.radius = 10
        
        self.alive = True


    # Update the player
    def update(self, input_state):
        if self.alive:

            #Use F=ma to get the acceleration
            if input_state.move_up:
                self.accel.y -= self.force_applied/self.mass * input_state.move_up

            if input_state.move_down:
                self.accel.y += self.force_applied/self.mass * input_state.move_down

            if input_state.move_left:
                self.accel.x -= self.force_applied/self.mass * input_state.move_left

            if input_state.move_right:
                self.accel.x += self.force_applied/self.mass * input_state.move_right


            # s = ut + 1/2 at^2
            self.pos += self.vel * constants.DT +  self.accel * 0.5 * constants.DT**2
            # v = u+at
            self.vel = (self.vel + self.accel * constants.DT) * (1-self.friction)
            self.accel = self.accel *  (1-self.friction)

            #Calculate the angle the deflector is facing by finding the vector between the mouse and the player and getting the angle of it
            self.deflector_angle = -(Vec2.from_tuple(input_state.mouse_pos) - self.pos).angle()

        else:
            print("Dead")
        
            


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
        # These are stored as member variables because they are useful in the detection of collisions between the deflector and bullets
        self.deflector_start = deflector_mid_point - vec_to_end 
        self.deflector_end = deflector_mid_point + vec_to_end

        # Draw the deflector
        pygame.draw.line(screen, (0,0,0), self.deflector_start.to_int().to_tuple(), self.deflector_end.to_int().to_tuple())



