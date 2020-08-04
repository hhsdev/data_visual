# _*_ coding: utf-8 _*_

from collections import deque 
from data_visual.node import Node

def pne(node):
    print('ProcessNodeEarly: %s' % node)

def pe(nodeA, nodeB):
    print('ProcessEdge: %s <---> %s' % (nodeA, nodeB))
    
def pnl(node):
    pass
    #print('ProcessNodeLate: %s' % node)

def breadth_first_search(graph, process_node_early, process_edge, process_node_late):
    if len(graph.nodes) == 0:
        return
    node_states = dict()
    queue = deque([ graph.nodes[0] ])
    node_states = { node: 'undiscovered' for node in graph.nodes }
    node_states[graph.nodes[0]] = 'discovered'
    while len(queue) > 0:
        current_node = queue.popleft()
        process_node_early(current_node)
        node_states[current_node] = 'processed'
        for neighbour in current_node.neighbours:
            if node_states[neighbour] != 'processed' or graph.directed:
                process_edge(current_node, neighbour)
            if node_states[neighbour] == 'undiscovered':
                queue.append(neighbour)
                node_states[neighbour] = 'discovered'
        process_node_late(current_node)

class DfsTraverser(object):
    def __init__(self):
        self.early_node_processor = self._do_nothing
        self.edge_processor = self._do_nothing
        self.late_node_processor = self._do_nothing
    
    def _do_nothing(self, node):
        pass

    def traverse(self, graph, starting_node):
        self.node_is_discovered = { node: False for node in graph.nodes }
        self.node_is_processed = { node: False for node in graph.nodes }
        self.graph = graph
        self.parent_of = { node: Node(-1) for node in graph.nodes }
        self._recursive_traverse(starting_node)

    def _recursive_traverse(self, node):
        self.node_is_discovered[node] = True
        self.early_node_processor(node)
        for neighbour in node.neighbours:
            if not self.node_is_discovered[neighbour]:
                self.parent_of[neighbour] = node
                self.edge_processor(node, neighbour)
                self._recursive_traverse(neighbour)

            elif not self.node_is_processed[neighbour] and self.parent_of[node] != neighbour:
                self.edge_processor(node, neighbour)

        self.late_node_processor(node)
        self.node_is_processed[node] = True

class Graph(object):
    def __init__(self, nodes, edges, directed=False):
        self.nodes = nodes
        self.directed = directed 
        self.add_edges(edges)
    
    def add_edge_between(self, nodeA, nodeB):
        """Creates an edge between two nodes."""
        if nodeA == nodeB:
            print('SimpleGraph does not support self connecting nodes')
            return
        nodeA.add_neighbour(nodeB)
        if not self.directed:
            nodeB.add_neighbour(nodeA)
  
    def add_edges(self, index_pairs):
        """Given a collection of index pairs, Adds
           an edge between each pair of nodes in `self.nodes`
           with such indices."""
        try:
            self._add_edges_no_check(index_pairs)
        except IndexError:
            print('IndexPair (%d, %d) is out of range'
                    % (index_pairs[0], index_pairs[1]))

    def _add_edges_no_check(self, index_pairs):
        for pair in index_pairs:
            self.add_edge_between(self.nodes[pair[0]],
                    self.nodes[pair[1]])

    def __len__(self):
        return len(self.nodes)      
    
if __name__ == "__main__":
    l = SimpleGraph([i for i in range(0, 6)], False)
    l.add_edges([ [0, 5], [0, 4], [0, 1], [1, 4], [1, 2], [2, 3], [3, 4] ])
    breadth_first_search(l, pne, pe, pnl)
    traverser = DfsTraverser()
    traverser.early_node_processor = pne
    traverser.late_node_processor = pnl
    traverser.edge_processor = pe
    traverser.traverse(l, l.nodes[0])


