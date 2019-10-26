# _*_ coding: utf-8 _*_

from data_visual.physical_object import PhysicalObject
from data_visual.force_emitter import ForceEmitter

class Attractor(ForceEmitter, PhysicalObject):
    min_distance = 4
    def __init__(self, intensity=1, position=0j):
        ForceEmitter.__init__(self)
        PhysicalObject.__init__(self, position)
        self.intensity = intensity
    
    def act_on(self, target):
        try:
            force = self.calculate_force_on(target)
            target.force += self.calculate_force_on(target)
        except ZeroDivisionError:
            target.force += 0j
       
    def calculate_force_on(self, target):
        distance = self.position - target.position
        distance_magnitude = abs(distance)

        if distance_magnitude < self.min_distance:
            distance_magnitude = self.min_distance

        force_magnitude = self.calculate_force_magnitude(
                target, distance_magnitude)
        force_unit_vector = distance / distance_magnitude

        return force_magnitude * force_unit_vector 

    def calculate_force_magnitude(self, target, distance):
        return (self.intensity * target.mass) / (distance ** 2)
    
    def __repr__(self):
        return 'Attractor(%s, %s)' % (self.intensity, self.position)




