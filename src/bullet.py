# Bullet object that enemies will shoot, just travels linearly
class Bullet:
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel
        self.radius = 3

    def update(self):
        self.pos += self.pos

    def render(self, screen):
        pygame.draw.circle(screen, (0,0,0), self.pos.to_int().to_tuple(), self.radius)

