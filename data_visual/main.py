# _*_ coding: utf-8 _*_

from data_visual.simulator import Simulator
from data_visual.physical_node import PhysicalNode
from data_visual.rubberband import Rubberband
from data_visual.attractor import Attractor
from data_visual.graph import Graph

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
    addRubberBands(simulator)
    addCenterGravity(simulator)

def addRepellers(simulator):
    for node in l.nodes:
        simulator.registerEmitter(node)

def addRubberBands(simulator)
    for edge in EDGES:
        nodeA = l.nodes[edge[0]]
        nodeB = l.nodes[edge[1]]
        simulator.registerEmitter(Rubberband(nodeA, nodeB))

def addAttracter(simulator):
    centerGravity = Attractor()
    centerGravity.isStatic = True
    simulator.registerEmitter(centerGravity)
    
if __name__ == "__main__":
    simulator = Simulator()
    addForceReceiversTo(simulator)
    addForceEmittersTo(simulator)

    simulator.simulate()
