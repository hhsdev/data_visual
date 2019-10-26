# _*_ coding: utf-8 _*_

import click
import networkx as nx

from data_visual.attractor import Attractor
from data_visual.graph import Graph
from data_visual.graph_artist import GraphArtist
from data_visual.setting import Setting
from data_visual.physical_node import PhysicalNode
from data_visual.rubberband import Rubberband
from data_visual.simulator import Simulator

from random import randrange

config = Setting(
    {
        "gravity": {"intensity": 2},
        "node": {"intensity": 50000},
        "edge": {"intensity": 0.04},
    })

#bg = nx.complete_graph(15)
#bg = nx.balanced_tree(2, 4)
#bg = nx.cycle_graph(25)
#bg = nx.dorogovtsev_goltsev_mendes_graph(5)
def rand_complex():
    return complex(randrange(0, 1000), randrange(0, 1000))

def translate(x, y):
    return x * 5 + y

def get_grid_graph(n, m):
    nx_graph = nx.grid_2d_graph(n, m)
    nodes = [PhysicalNode(translate(x,y), rand_complex(), config["node"]["intensity"])
                for (x,y) in nx_graph.nodes]
    edges = [[translate(a, b), translate(c, d)]
                for ((a, b), (c, d)) in nx_graph.edges]
    return (nodes, edges)

NODES, EDGES = get_grid_graph(5, 5)

#bg = nx.petersen_graph()
#bg = nx.sedgewick_maze_graph()
#bg = nx.tetrahedral_graph()
#NODES = [PhysicalNode(label, randVec2(), config["node"]["intensity"]) for label in bg.nodes]
#EDGES = bg.edges
#NODES = [PhysicalNode(0, randVec2(), 1), PhysicalNode(1, randVec2(), 1)]
#EDGES = [(0,1)]
print("  Simulating %s nodes and %s edges..." % (len(NODES), len(EDGES)))
graph = Graph(NODES, EDGES, False)

def add_force_receivers_to(simulator):
    for node in graph.nodes:
        simulator.register_receiver(node)

def add_center_gravity(simulator):
    center_gravity = Attractor(config["gravity"]["intensity"])
    simulator.register_emitter(center_gravity)

def add_force_emitters_to(simulator):
    add_repellers(simulator)
    add_rubber_bands(simulator)
    add_center_gravity(simulator)

def add_repellers(simulator):
    for node in graph.nodes:
        simulator.register_emitter(node)

def add_rubber_bands(simulator):
    for edge in EDGES:
        nodeA = graph.nodes[edge[0]]
        nodeB = graph.nodes[edge[1]]
        simulator.register_emitter(Rubberband(nodeA, nodeB, config["edge"]["intensity"]))

def simulate_with_progress_bar(simulator):
    with click.progressbar(length=simulator.settings["max_ticks"]) as bar:
        update_progress = lambda simulator : bar.update(simulator.ticks)
        simulator.event_listeners["tick"].append(update_progress)
        simulator.simulate()


if  __name__ == "__main__":
    artist_settings = Setting({
        "background": "white",
        "width": 1000,
        "height": 1000,
        "node": {"color": (0x46, 0x63, 0x65)},
        "edge": {"color": (0x9d, 0x99, 0xb6)},
    })

    artist = GraphArtist(artist_settings)

    simulator = Simulator()
    add_force_receivers_to(simulator)
    add_force_emitters_to(simulator)

    frames = []
    draw_frame = lambda stud: frames.append(artist.draw(graph))
    simulator.event_listeners["tick"].append(draw_frame)

    simulate_with_progress_bar(simulator)
    image = artist.draw(graph)

    print("  Writing gif... ", end="", flush=True)
    frames[0].save(
            './images/move.gif',
            format='GIF',
            append_images=frames[1:],
            save_all=True,
            duration=100,
            loop=0)

    print("saved to ./images/move.gif", flush=True)
    print("  Writing final image... ", end="", flush=True)
    image.save("./images/result.png")
    print("saved to ./images/result.png", flush=True)
