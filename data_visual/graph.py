from collections import deque 
from data_visual.node import Node

def pne(node):
    print('ProcessNodeEarly: %s' % node)

def pe(nodeA, nodeB):
    print('ProcessEdge: %s <---> %s' % (nodeA, nodeB))
    
def pnl(node):
    pass
    #print('ProcessNodeLate: %s' % node)

def breadthFirstSearch(graph, processNodeEarly, processEdge, processNodeLate):
    if len(graph.nodes) == 0:
        return
    nodeStates = dict()
    queue = deque([ graph.nodes[0] ])
    nodeStates = { node: 'undiscovered' for node in graph.nodes }
    nodeStates[graph.nodes[0]] = 'discovered'
    while len(queue) > 0:
        currentNode = queue.popleft()
        processNodeEarly(currentNode)
        nodeStates[currentNode] = 'processed'
        for neighbour in currentNode.neighbours:
            if nodeStates[neighbour] != 'processed' or graph.directed:
                processEdge(currentNode, neighbour)
            if nodeStates[neighbour] == 'undiscovered':
                queue.append(neighbour)
                nodeStates[neighbour] = 'discovered'
        processNodeLate(currentNode)

class DfsTraverser(object):
    def __init__(self):
        self.earlyNodeProcessor = self._doNothing
        self.edgeProcessor = self._doNothing
        self.lateNodeProcessor = self._doNothing
    
    def _doNothing(self, node):
        pass

    def traverse(self, graph, startingNode):
        self.nodeIsDiscovered = { node: False for node in graph.nodes }
        self.nodeIsProcessed = { node: False for node in graph.nodes }
        self.graph = graph
        self.parentOf = { node: Node(-1) for node in graph.nodes }
        self._recursiveTraverse(startingNode)

    def _recursiveTraverse(self, node):
        self.nodeIsDiscovered[node] = True
        self.earlyNodeProcessor(node)
        for neighbour in node.neighbours:
            if not self.nodeIsDiscovered[neighbour]:
                self.parentOf[neighbour] = node
                self.edgeProcessor(node, neighbour)
                self._recursiveTraverse(neighbour)

            elif not self.nodeIsProcessed[neighbour] and self.parentOf[node] != neighbour:
                self.edgeProcessor(node, neighbour)

        self.lateNodeProcessor(node)
        self.nodeIsProcessed[node] = True

class SimpleGraph(object):
    def __init__(self, nodes, edges, directed=False):
        self.nodes = nodes
        self.addEdges(edges)
        self.directed = directed 
        self.simple = directed 
    
    def addEdgeBetween(self, nodeA, nodeB):
        """Creates an edge between two nodes."""
        if nodeA == nodeB:
            print('SimpleGraph does not support self connecting nodes')
            return
        nodeA.addNeighbour(nodeB)
        if not self.directed:
            nodeB.addNeighbour(nodeA)
  
    def addEdges(self, indexPairs):
        """Given a collection of index pairs, Adds
           an edge between each pair of nodes in `self.nodes`
           with such indices."""
        try:
            self._addEdgesNoCheck(indexPairs)
        except IndexError:
            print('IndexPair (%d, %d) is out of range'
                    % (indexPair[0], indexPair[1]))

    def _addEdgesNoCheck(self, indexPairs):
        for pair in indexPairs:
            self.addEdgeBetween(self.nodes[pair[0]],
                    self.nodes[pair[1]])

    def __len__(self):
        return len(self.nodes)      
    
if __name__ == "__main__":
    l = SimpleGraph([i for i in range(0, 6)], False)
    l.addEdges([ [0, 5], [0, 4], [0, 1], [1, 4], [1, 2], [2, 3], [3, 4] ])
    breadthFirstSearch(l, pne, pe, pnl)
    print('\n\n')
    traverser = DfsTraverser()
    traverser.earlyNodeProcessor = pne
    traverser.lateNodeProcessor = pnl
    traverser.edgeProcessor = pe
    traverser.traverse(l, l.nodes[0])

