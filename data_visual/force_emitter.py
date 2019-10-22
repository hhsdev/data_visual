# _*_ coding: utf-8 _*_

from data_visual.physical_object import PhysicalObject 

class ForceEmitter(PhysicalObject):
    """Base class that can exert force"""

    def __init__(self):
       PhysicalObject.__init__(self)

    def registerTo(self, simulator):
        simulator.forces.append(self)
    
    def actOn(self, thing):
        raise NotImplementedError

