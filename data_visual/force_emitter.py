# _*_ coding: utf-8 _*_

class ForceEmitter(object):
    """Base class that can exert force"""

    def __init__(self):
        return

    def act_on(self, thing):
        raise NotImplementedError
