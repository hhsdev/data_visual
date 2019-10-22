# _*_ coding: utf-8 _*_

from data_visual.force_emitter import ForceEmitter
from data_visual.vec2 import Vec2

class Repeller(ForceEmitter):
    def __init__(self, intensity):
        ForceEmitter.__init__(self)
        self.intensity = intensity
    
    def actOn(self, target):
        forceToTarget = self.calculateForceTo(target)
        target.acceleration = forceToTarget / target.mass
       
    def calculateForceTo(self, target):
        distanceVector = target.position - self.position
        distanceFromTarget = abs(distanceVector)

        if distanceFromTarget > 0:
            forceMagnitude = self.calculateForceMagnitude(target, distanceFromTarget)
            forceUnitVector = distanceVector / distanceFromTarget
        else:
            forceMagnitude = self.calculateForceMagnitude(target, 0.1)
            forceUnitVector = Vec2(1.0, 0)

        return forceMagnitude * forceUnitVector 

    def calculateForceMagnitude(self, target, distance):
        return (self.intensity * target.mass) / (distance ** 2)

