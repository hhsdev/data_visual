# _*_ coding: utf-8 _*_
from data_visual.fr.node import FrNode
from data_visual.fr.rubberband import FrRubberband
from random import randrange
from data_visual.fr.common import calculate_k


def build_from_nx(graph, config):
    width = config["width"]
    height = config["height"]

    def random_position(w, h): return complex(randrange(w), randrange(h))

    num_nodes = len(graph.nodes)

    k = calculate_k(config["c"], width * height, num_nodes)
    nodes = [FrNode(node, random_position(width, height),
                    width, height, k) for node in graph.nodes]
    edges = [FrRubberband(nodes[a], nodes[b], k) for a, b in graph.edges]

    return (nodes, edges)
