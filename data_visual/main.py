# _*_ coding: utf-8 _*_

from data_visuals.simulator import Simulator
from data_visuals.physical_node import PhysicalNode
from data_visuals.stretcher import Stretcher 
from data_visuals.attractor import Attractor
from data_visuals.graph import Graph

NUM_NODES = 6
LABELS = [i for i in range(0, NUM_NODES)]
EDGES = [[0, 5], [0, 4], [0, 1], [1, 4], [1, 2], [2, 3], [3, 4]]

l = SimpleGraph(
        [PhysicalNode(label) for label in LABELS],
        CONNECTIONS,
        False)

def addForceReceiversTo(simulator):
    for node in l.nodes:
        simulator.registerReceiver(node)

def addForceEmittersTo(simulator):
    addRepellers(simulator)
    addStretchers(simulator)
    addCenterGravity(simulator)

def addRepellers(simulator):
    for node in l.nodes:
        simulator.registerEmitter(node)

def addStretchers(simulator)
    for edge in EDGES:
        nodeA = l.nodes[edge[0]]
        nodeB = l.nodes[edge[1]]
        simulator.registerEmitter(Stretcher(nodeA, nodeB))

def addAttracter(simulator):
    centerGravity = Attractor()
    centerGravity.isStatic = True
    simulator.registerEmitter(centerGravity)
    
if __name__ == "__main__":
    simulator = Simulator()
    addForceReceiversTo(simulator)
    addForceEmittersTo(simulator)

    simulator.simulate()
