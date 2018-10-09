import pygame
import math
from vec2 import Vec2

# Bullet object that enemies will shoot, just travels linearly
class Bullet:
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel
        self.radius = 5
        
        self.colour = (0,0,0)
        self.reflected_colour = (255,0,0)


        #Bool of whether or not the boolean has been reflected off of the player's deflector
        self.reflected = False
        self.alive = True

    def update(self, state_obj):
        self.pos += self.vel
        self.collide_with_enemy(state_obj.enemies)
        self.collide_with_player(state_obj.player)
        self.collide_with_deflector(state_obj.player)
        if self.pos.x + self.radius < 0 or self.pos.x - self.radius > state_obj.width or self.pos.y + self.radius < 0 or self.pos.y - self.radius > state_obj.height:    
            self.alive = False
            
        #if the bullet isn't alive delete it   
        if not self.alive:
            state_obj.bullets.remove(self)
            del self

        
        

    #Handle collisions with the deflector
    def collide_with_deflector(self, player):

        #If the bullet has already been reflected, don't reflect it again
        if self.reflected:
            return


        #http://paulbourke.net/geometry/pointlineplane/

        u = (((self.pos.x-player.deflector_start.x) * (player.deflector_end.x-player.deflector_start.x) +
              (self.pos.y-player.deflector_start.y) * (player.deflector_end.y-player.deflector_start.y))/
             (player.deflector_end-player.deflector_start).magnitude2())

        j = player.deflector_end-player.deflector_start

        #This means collision is not within line segment
        if (u <= 0 or u > 1):
            return

        point_of_intersection = (player.deflector_end-player.deflector_start)*u + player.deflector_start
        to_wall_vector = point_of_intersection - self.pos
        distance_to_wall = to_wall_vector.magnitude()

        if self.radius > distance_to_wall:
            collision_depth = self.radius - distance_to_wall

            normalised_wall_vector = (to_wall_vector).normalise()

            self.pos += normalised_wall_vector * collision_depth

            #https://stackoverflow.com/a/573206
            #But have u=x, w=y for the sake of not reusing variable name 'u'

            x = normalised_wall_vector * (self.vel.dp(normalised_wall_vector))
            y = self.vel-x

            self.vel = y - x
            self.reflected = True

    def collide_with_enemy(self, enemies):
        for enemy in enemies:
            #If the bullet has been deflected and is colliding with an enemy set the bullet and enemy to not alive
            if self.reflected and (enemy.pos-self.pos).magnitude2() <= (enemy.radius + self.radius)**2:
                self.alive = False
                enemy.alive = False

    def collide_with_player(self, player):
        #If the bullet has been deflected and is colliding with the player set the bullet and player to not alive
        if not self.reflected and (player.pos-self.pos).magnitude2() <= (player.radius + self.radius)**2:
            self.alive = False
            player.alive = False


    def render(self, screen):
        pygame.draw.circle(screen, self.reflected_colour if self.reflected else self.colour, self.pos.to_int().to_tuple(), self.radius)

