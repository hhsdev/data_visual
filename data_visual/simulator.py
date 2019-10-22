# _*_ coding: utf-8 _*_

class Simulator(object):
    def __init__(self):
        self.forceEmitters = []
        self.forceReceivers = []
        self.eventListeners = {}
        self.ticks = 0

    def simulate(self):
        while not self.shouldStopSimulation():
            self.simulateTick()

    def simulateTick(self):
        for emitter in self.forceEmitters:
            for receiver in self.forceReceivers:
                emitter.actOn(receiver)

        for receiver in self.forceReceivers:
            receiver.move()

        for listener in self.eventListeners['tick']:
            listener(self)

        self.ticks += 1
    
    def shouldStopSimulation():
        threshold = 0.1
        if self.ticks < 5:
            return False
        for receiver in self.forceReceivers:
            if receiver.velocity > threshold:
                return False
        return True

