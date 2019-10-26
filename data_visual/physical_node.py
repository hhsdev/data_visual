# _*_ coding: utf-8
from data_visual.node import Node
from data_visual.repeller import Repeller 

class PhysicalNode(Node, Repeller):
    def __init__(self, label, position, intensity=1, mass=1):
        Node.__init__(self, label)
        Repeller.__init__(self, position, intensity, mass)

    def __repr__(self):
        return 'PhysicalNode(%s, %s, %s)' % (self.label, self.intensity, self.position)

    def __str__(self):
        return 'PhysicalNode(%s, %s, %s)' % (self.label, self.intensity, self.position)
