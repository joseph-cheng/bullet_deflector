from vec2 import Vec2

class Enemy:
    def __init__(self, x, y, c):
        self.pos = Vec2(x, y)
        self.vel = Vec2(0, 0)
        self.colour = c
        
        self.radius = 10

    def update(self):
##      Updates the enemys position with their velocity  
        self.pos += self.vel

    def render(self, screen):        
##      Draws the enemy
        pygame.draw.circle(screen, (self.colour), self.pos.to_int().to_tuple(), self.radius)
        
        
