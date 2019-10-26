# _*_ coding: utf-8 _*_
from data_visual.setting import Setting

class Simulator(object):
    defaults = Setting({
        'threshold': 0.1,
        'min_ticks': 5,
        'max_ticks': 300
    })

    def __init__(self, settings=Setting({})):
        self.settings = self.defaults
        self.settings.override(settings)

        self.ticks = 0

        self.event_listeners = { 'tick': [] }
        self.force_receivers = []
        self.force_emitters = []

    def simulate(self):
        while not self.should_stop():
            self.simulate_tick()
    
    def simulate_tick(self):
        for receiver in self.force_receivers:
            receiver.force = 0j
            receiver.acceleration = 0j

        for emitter in self.force_emitters:
            for receiver in self.force_receivers:
                emitter.act_on(receiver)

        for receiver in self.force_receivers:
            receiver.react_to_force()

        for listener in self.event_listeners["tick"]:
            listener(self)
        self.ticks += 1
    
    def should_stop(self):
        if self.ticks < self.settings["min_ticks"]:
            return False

        if self.ticks > self.settings["max_ticks"]:
            return True

        for receiver in self.force_receivers:
            if abs(receiver.velocity) > self.settings["threshold"]:
                return False
        return True
    
    def register_emitter(self, emitter):
        self.force_emitters.append(emitter)

    def register_receiver(self, receiver):
        self.force_receivers.append(receiver)

