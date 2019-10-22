# _*_ coding: utf-8 _*_

from data_visual.physical_object import PhysicalObject
from data_visual.force_emitter import ForceEmitter
from data_visual.vec2 import Vec2

class Attractor(ForceEmitter, PhysicalObject):
    def __init__(self, intensity=1, position=Vec2(0,0)):
        ForceEmitter.__init__(self)
        PhysicalObject.__init__(self, position)
        self.intensity = intensity
    
    def actOn(self, target):
        try:
            target.force += self.calculateForceOn(target)
        except ZeroDivisionError:
            target.force += Vec2(0, 0)
       
    def calculateForceOn(self, target):
        distanceVector = self.position - target.position
        distanceFromTarget = abs(distanceVector)
        
        forceMagnitude = self.calculateForceMagnitude(
                target, distanceFromTarget)
        forceUnitVector = distanceVector / distanceFromTarget
        return forceMagnitude * forceUnitVector 

    def calculateForceMagnitude(self, target, distance):
        return (self.intensity * target.mass) / (distance ** 2)

