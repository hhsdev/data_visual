# _*_ coding: utf-8 _*_

from PIL import Image, ImageDraw
from data_visual.setting import Setting

class GraphArtist(object):
    """
        Takes graph data and outputs an image.
    """

    defaults = Setting({
                "width": 500,
                "height": 500,
                "background": (0x88, 0x88, 0x88),
                "node": {
                         "color": "red",
                         "radius": 10,
                        },
                "edge": {"color": "blue"}
               })

    def __init__(self, settings):
        object.__init__(self)
        self.settings = self.defaults
        self.settings.override(settings)

    def draw(self, graph):
        self.image = Image.new("RGB",
                (self.settings["width"], self.settings["height"]),
                 self.settings["background"])
        self.pen = ImageDraw.Draw(self.image)

        for node in graph.nodes:
            for neighbour in node.neighbours:
                self.drawEdge(node, neighbour)

        for node in graph.nodes:
            self.drawNode(node)
        return self.image

    def drawEdge(self, endPointA, endPointB):
        centerA = endPointA.position
        centerB = endPointB.position

        self.pen.line(
                ((centerA.real, centerA.imag), (centerB.real, centerB.imag)),
                fill=self.settings["edge"]["color"])

    def drawNode(self, node):
        center = node.position
        radius = self.settings["node"]["radius"]

        x0 = center.real - radius
        x1 = center.real + radius
        y0 = center.imag - radius
        y1 = center.imag + radius

        self.pen.ellipse(
                (x0, y0, x1, y1),
                fill=self.settings["node"]["color"])
