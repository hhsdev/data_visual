# _*_ coding: utf-8 _*_

import click
import networkx as nx
import cProfile

from data_visual.attractor import Attractor
from data_visual.graph import Graph
from data_visual.graph_artist import GraphArtist
from data_visual.setting import Setting
from data_visual.physical_node import PhysicalNode
from data_visual.rubberband import Rubberband
from data_visual.simulator import Simulator
from data_visual.fr.builder import build_from_nx

from random import randrange
from unittest.mock import MagicMock
from PIL import ImageFilter


config = Setting(
    {
        "gravity": {"intensity": 1e7},
        "node": {"intensity": 7000},
        "edge": {"intensity": 0.04},
    })

fr_config = Setting(
    {
        "width": 500,
        "height": 500,
        "c": 0.5
    })


def rand_complex():
    return complex(randrange(0, 500), randrange(0, 500))


def translate(x, y):
    return x * 10 + y


def get_grid_graph(n, m):
    nx_graph = nx.grid_2d_graph(n, m)
    nodes = [PhysicalNode(translate(x, y), rand_complex(), config["node"]["intensity"])
             for (x, y) in nx_graph.nodes]
    edges = [[translate(a, b), translate(c, d)]
             for ((a, b), (c, d)) in nx_graph.edges]
    return (nodes, edges)


# -------------------- bg ----------------------
# bg = nx.complete_graph(20)
# bg = nx.balanced_tree(2, 7)
# bg = nx.cycle_graph(125)
# bg = nx.sedgewick_maze_graph()
# bg = nx.tetrahedral_graph()
# bg = nx.petersen_graph()
bg = nx.dorogovtsev_goltsev_mendes_graph(4)


NODES, EDGES = build_from_nx(bg, fr_config)

print("  Simulating %s nodes and %s edges..." % (len(NODES), len(EDGES)))
graph = Graph(NODES, bg.edges, False)


def add_force_receivers_to(simulator):
    for node in graph.nodes:
        simulator.register_receiver(node)


def add_center_gravity(simulator):
    center_gravity = Attractor(config["gravity"]["intensity"])
    simulator.register_emitter(center_gravity)


def add_force_emitters_to(simulator):
    add_repellers(simulator)
    add_rubber_bands(simulator)
    # add_center_gravity(simulator)


def add_repellers(simulator):
    for node in graph.nodes:
        simulator.register_emitter(node)


def add_rubber_bands(simulator):
    for edge in EDGES:
        simulator.event_listeners["start"].append(edge)


def simulate_with_progress_bar(simulator):
    with click.progressbar(length=simulator.settings["max_ticks"]) as bar:
        def update_progress(simulator): bar.update(1)
        simulator.event_listeners["tick"].append(update_progress)
        simulator.run(realistic=False)


frames = []


def gif_on_end(simulator):
    print("\n  Writing gif... ", end="", flush=True)
    frames[0].save(
        "./images/move.gif",
        format="GIF",
        append_images=frames[1:],
        save_all=True,
        duration=100,
        loop=0)
    print("saved to ./images/move.gif", flush=True)


def enable_gif(artist, simulator):
    simulator.event_listeners["tick"].append(
        lambda _: frames.append(artist.draw(graph)))
    simulator.event_listeners["end"].append(gif_on_end)


if __name__ == "__main__":
    artist_settings = Setting({
        "background": "black",
        "width": fr_config["width"],
        "height": fr_config["height"],
        "node": {"radius": 5, "color": 'white'},
        "edge": {"color": 'gray'}
    })

    artist = GraphArtist(artist_settings)

    simulator = Simulator()

    add_force_receivers_to(simulator)
    add_force_emitters_to(simulator)
    enable_gif(artist, simulator)

    simulate_with_progress_bar(simulator)
    image = artist.draw(graph)
    image = image.filter(ImageFilter.SMOOTH)
    print("  Writing final image... ", end="", flush=True)
    image.save("./images/result.png")
    print("saved to ./images/result.png", flush=True)
