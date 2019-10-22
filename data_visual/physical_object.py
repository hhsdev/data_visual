# _*_ coding: utf-8 _*_
from data_visual.vec2 import Vec2

class PhysicalObject(object):
    def __init__(self, position=Vec2(0, 0), mass=1):
        self.position = position
        self.mass = mass
        self.force = Vec2()
        self.acceleration = Vec2()
        self.velocity = Vec2()

    def moveBy(self, thisMuch):
        self.position += thisMuch
     
    def reactToForce(self):
        try:
            self.acceleration = self.force / self.mass
        except ZeroDivisionError:
            self.acceleration = 0
        self.move()

    def move(self):
        self.velocity += self.acceleration
        self.position += self.velocity
