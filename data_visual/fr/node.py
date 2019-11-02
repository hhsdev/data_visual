# _*_ coding: utf-8

from data_visual.fr.repeller import FrRepeller
from data_visual.node import Node
from random import random

class FrNode(Node, FrRepeller):
    def __init__(self, label, position, width, height, intensity):
        Node.__init__(self, label)
        FrRepeller.__init__(self, position, intensity)
        self.width = width
        self.height = height
        self.times_moved = 0

    def react_to_force(self):
        max_allowed_displacement = self._get_max_displacement()
        displacement_from_force = abs(self.force)
        real_displacement = self.unit(
            self.force) * min(max_allowed_displacement, displacement_from_force)
        self.position += real_displacement
        self.keep_in_bound()
        self.times_moved += 1

    def _get_max_displacement(self):
        base_limit = self.width / 10
        return base_limit / 1.08 ** self.times_moved

    def keep_in_bound(self):
        if self.position.real <= 0:
            self.position = complex(random(), self.position.imag)
        elif self.position.real >= self.width:
            self.position = complex(self.width - random(), self.position.imag)

        if self.position.imag <= 0:
            self.position = complex(self.position.real, random())
        elif self.position.imag >= self.height:
            self.position = complex(self.position.real, self.height - random())
