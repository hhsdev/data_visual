# _*_ coding: utf-8 _*_
class PhysicalObject(object):
    timestep = 1
    def __init__(self, position=0j, mass=1):
        self.position = position
        self.mass = mass

        self.force = 0j
        self.acceleration = 0j 
        self.velocity = 0j

    def move_by(self, this_much):
        self.position += this_much
     
    def react_to_force(self):
        try:
            self.acceleration = self.force / self.mass
        except ZeroDivisionError:
            self.acceleration = 0j
        self.move()

    def move(self):
        self.velocity += (self.acceleration * self.timestep)
        self.position += (self.velocity * self.timestep)
