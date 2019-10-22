# _*_ coding: utf-8 _*_

class Node(object):
    """Node of a graph"""

    def __init__(self, label):
        self.label = label
        self.neighbours = [] 

    def isNeighboursWith(self, node):
        return node in self.neighbours

    def addNeighbour(self, node):
        if not self.isNeighboursWith(node):
            self.addNeighbourNoCheck(node)
   
    def addNeighbourNoCheck(self, node):
        self.neighbours.append(node)

    def __repr__(self):
        return str(self) 

    def __str__(self):
        return 'Node(%s)' % (self.label+1)

    def __eq__(self, other):
        return self.label == other.label
    
    def __hash__(self):
        return hash(self.label)

