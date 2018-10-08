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
        return self.x * other.x + self.y * other.y

    # Get magnitude
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def magnitude2(self):
        return self.x**2 + self.y**2

    #Get angle of vector in radians
    def angle(self):
        return math.atan2(self.y, self.x)

    # Returns unit vector in same direction as self
    def normalise(self):
        return self/(self.magnitude())

    # Turns the vec into a tuple, useful for pygame
    def to_tuple(self):
        return (self.x, self.y)

    def to_int(self):
        return Vec2(int(self.x), int(self.y))

    #Get a Vec2 from a tuple
    def from_tuple(tup):
        return Vec2(tup[0], tup[1])

    # Returns a copy of itself
    def copy(self):
        return Vec2(self.x, self.y)
