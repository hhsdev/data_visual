# _*_ coding: utf-8 _*_

from data_visual.repeller import Repeller
from data_visual.fr.common import calculate_k

class FrRepeller(Repeller):
    def __init__(self, position, intensity):
        Repeller.__init__(self, position, intensity)
    
    def calculate_force_on(self, target):
        distance = target.position - self.position
        force_magnitude = self.intensity ** 2 / abs(distance)
        return self.unit(distance) * force_magnitude
