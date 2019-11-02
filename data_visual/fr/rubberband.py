# _*_ coding: utf-8 _*_

from data_visual.rubberband import Rubberband
from data_visual.fr.common import calculate_k
from math import sqrt

class FrRubberband(Rubberband):
    def __init__(self, a, b, intensity):
        Rubberband.__init__(self, a, b, intensity)

    def calculate_force_on(self, target):
        other_target = self._get_other_target(target)
        distance = other_target.position - target.position
        force_magnitude = abs(distance) ** 2 / self.intensity
        return force_magnitude * self.unit(distance)
