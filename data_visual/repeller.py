# _*_ coding: utf-8 _*_

from data_visual.force_emitter import ForceEmitter
from data_visual.physical_object import PhysicalObject

class Repeller(ForceEmitter, PhysicalObject):
    min_distance = 0.05
    def __init__(self, position, intensity=1, mass=1):
        ForceEmitter.__init__(self)
        PhysicalObject.__init__(self, position, mass)
        self.intensity = intensity
    
    def act_on(self, target):
        try:
            force = self.calculate_force_on(target)
            target.force += force
        except ZeroDivisionError:
            pass
       
    def calculate_force_on(self, target):
        distance = target.position - self.position
        distance_magnitude = abs(distance)
        if distance_magnitude < self.min_distance:
            distance_magnitude = self.min_distance

        force_magnitude = self.calculate_force_magnitude(
                target, distance_magnitude)
        force_unit_vector = distance / distance_magnitude
        return force_magnitude * force_unit_vector 

    def calculate_force_magnitude(self, target, distance):
        return (self.intensity * target.mass) / (distance ** 2)


