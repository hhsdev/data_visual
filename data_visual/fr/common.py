# _*_ coding: utf-8 _*_
from math import sqrt

def calculate_k(c, area, num_nodes):
    return c * sqrt(area / num_nodes)
