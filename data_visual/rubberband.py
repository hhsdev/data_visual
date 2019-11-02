# _*_ coding: utf-8 _*_

from data_visual.force_emitter import ForceEmitter
from math import sqrt

class Rubberband(ForceEmitter):
    def __init__(self, a, b, intensity=0.1):
        ForceEmitter.__init__(self)
        self.a = a
        self.b = b
        self.intensity = intensity
    
    def act_on(self, target):
        if target != self.a and target != self.b:
            return
        force = self.calculate_force_on(target)
        target.force += force
    
    def __call__(self, _):
        self.act_on(self.a)
        self.act_on(self.b)

    def calculate_force_on(self, target):
        other_target = self._get_other_target(target)
        distance_vector = other_target.position - target.position
        spring_force = distance_vector * self.intensity
        dampening_force = self.calculate_dampening(target)
        return spring_force + dampening_force
    
    def calculate_dampening(self, target):
        return -2 * sqrt(self.intensity) * target.velocity

    def _get_other_target(self, target):
        if target == self.a:
            return self.b
        return self.a

    def __str__(self):
        return 'Rubber(%s, %s, %s)' % (self.a.label, self.b.label, self.intensity)
        

