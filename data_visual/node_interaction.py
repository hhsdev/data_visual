# _*_ coding: utf-8 _*_

class NodeInteraction(object):
    """Controls the interactions between nodes."""
    
    def __init__(self, graph):
        self.nodes = graph.nodes

    def act(self):
        for emitter in self.nodes:
            for recipient in self.nodes:
                emitter.act_on(recipient)
