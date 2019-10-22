# _*_ coding: utf-8 _*_

from data_visual.physical_object import PhysicalObject 
from data_visual.vec2 import Vec2

class ForceEmitter(object):
    """Base class that can exert force"""

    def __init__(self, position=Vec2(0, 0)):
       PhysicalObject.__init__(self)

    def actOn(self, thing):
        raise NotImplementedError

