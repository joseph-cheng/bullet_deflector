import math

# 2D Vector
class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Operator overload for +
    def __add__(self, other):
        return Vec2(self.x+other.x, self.y+other.y)

    # Operator overload for +=
    def __iadd__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vec2(x, y)
    
    # Operator overload for -
    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    # Operator overload for *
    def __mul__(self, scale):
        return Vec2(self.x*scale, self.y*scale)

    # Operator overload for /
    def __truediv__(self, scale):
        return Vec2(self.x/scale, self.y/scale)

    # Dot product
    def dp(self, other):
        return Vec2(self.x * other.x, self.y * other.y)

    # Get magnitude
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)
