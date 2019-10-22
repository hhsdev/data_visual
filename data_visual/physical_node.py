# _*_ coding: utf-8
from node import Node
from repeller import Repeller 


class PhysicalNode(Node, Repeller):
    def __init__(self, label, position=Point(0, 0)):
        Node.__init__(self, label)
        Repeller.__init__(self, position)
        self.node = node
