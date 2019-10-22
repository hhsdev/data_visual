# _*_ coding: utf-8 _*_
from math import hypot

class Vec2(object):
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vec2(self.x + other, self.y + other)
        return Vec2(self.x + other.x, self.y + other.y)

    def __radd__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vec2(self.x + other, self.y + other)
        return Vec2(self.x + other.x, self.y + other.y)
    
    def __iadd__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.x += other
            self.y += other
        else:
            self.x += other.x
            self.y += other.y
        return self
    
    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vec2(self.x - other, self.y - other)
        return Vec2(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.x -= other
            self.y -= other
        else:
            self.x -= other.x
            self.y -= other.y
        return self

    def __mul__(self, other):
        return Vec2(self.x * other, self.y * other)

    def __rmul__(self, other):
        return Vec2(self.x * other, self.y * other)

    def __imul__(self, other):
        self.x *= other
        self.y *= other
        return self
    
    def __truediv__(self, other):
        return Vec2(self.x / other, self.y / other)

    def __rtruediv__(self, other):
        return Vec2(self.x / other, self.y / other)

    def __itruediv__(self, other):
        self.x /= other
        self.y /= other
        return self
    
    def __abs__(self):
        return hypot(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __neq__(self, other):
        return not self == other

    def __repr__(self):
        return 'Vec2(%r, %r)' % (self.x, self.y)

