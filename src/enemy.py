from vec2 import Vec2
import bullet
import pygame
import math

class Enemy:
    def __init__(self, x, y, c):
        self.pos = Vec2(x, y)
        self.vel = Vec2(0, 0)
        self.colour = c
        
        self.radius = 10

        #Amount of ticks between shooting
        self.max_shoot_timer = 100
        self.shoot_timer = self.max_shoot_timer

        self.alive = True

    def update(self, state_obj):
        self.shoot_timer -= 1

##      Updates the enemys position with their velocity  
        self.pos += self.vel

        # If the enemy needs to shoot, make them shoot and reset the shoot timer
        if self.shoot_timer == 0:
            self.shoot_at_player(state_obj)
            self.shoot_timer = self.max_shoot_timer

        if not self.alive:
            state_obj.enemies.remove(self)
            del self

    def shoot_at_player(self, state_obj):
        angle = (state_obj.player.pos - self.pos).angle()
        state_obj.unreflected_bullets.append(bullet.Bullet(self.pos.copy(), Vec2(math.cos(angle), math.sin(angle))))


    def render(self, screen):        
##      Draws the enemy
        pygame.draw.circle(screen, (self.colour), self.pos.to_int().to_tuple(), self.radius)
        
        
