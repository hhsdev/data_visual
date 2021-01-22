# _*_ coding: utf-8 _*_
from data_visual.setting import Setting

class Simulator(object):
    defaults = Setting({
        'threshold': 0.001,
        'min_ticks': 5,
        'max_ticks': 200
    })
    def __init__(self, settings=Setting()):
        self.settings = self.defaults
        self.settings.override(settings)

        self.ticks = 0

        self.event_listeners = { "tick": [], "end": [], "start": [] }
        self.force_receivers = []
        self.force_emitters = []
        self.late_force_emitters = []
    

    def run(self, *, realistic=True):
        while not self.should_stop():
            self.simulate_tick(realistic)
        self.emit_event("end")
    
    def run_iter(self, *, realistic=True):
        while not self.should_stop():
            yield self.simulate_tick(realistic)

    def emit_event(self, event_name):
        for listener in self.event_listeners[event_name]:
            listener(self)

    def simulate_tick(self, realistic):
        self.reset_receivers_kinetics(realistic)
        
        self.emit_event("start")
        self.interact(self.force_emitters, self.force_receivers)
        self.interact(self.late_force_emitters, self.force_receivers)

        self.emit_event("tick")
        self.ticks += 1
    
    def interact(self, emitters, receivers):
        for emitter in self.force_emitters:
            for receiver in self.force_receivers:
                emitter.act_on(receiver)
        
        if len(emitters) != 0:
            for receiver in self.force_receivers:
                receiver.react_to_force()
        
    def reset_receivers_kinetics(self, realistic):
        for receiver in self.force_receivers:
            receiver.force = 0j
            receiver.acceleration = 0j
            if not realistic:
                receiver.velocity = 0j

    def should_stop(self):
        if self.ticks < self.settings["min_ticks"]:
            return False

        if self.ticks > self.settings["max_ticks"]:
            return True
        return False
        for receiver in self.force_receivers:
            if abs(receiver.velocity) > self.settings["threshold"]:
                return False
        return True
    
    def register_emitter(self, emitter):
        self.force_emitters.append(emitter)

    def register_receiver(self, receiver):
        self.force_receivers.append(receiver)

