# _*_ coding: utf-8 _*_

from data_visual.physical_object import PhysicalObject
from data_visual.vec2 import Vec2

import pytest

@pytest.fixture
def physical_object():
    return PhysicalObject()

def test_move_by(physical_object):
    physical_object.move_by(2 + 2j)
    assert physical_object.position == 2 + 2j

    physical_object.move_by(2 + 2j)
    assert physical_object.position == 4 + 4j

def test_linear_move(physical_object):
    physical_object.velocity = 1 + 1j
    physical_object.move()
    assert physical_object.position == 1 + 1j
    physical_object.move()
    physical_object.move()
    assert physical_object.position == 3 + 3j

def test_constant_accleration_move(physical_object):
    physical_object.acceleration = 1 + 0j

    physical_object.move()
    assert physical_object.velocity == 1 + 0j
    assert physical_object.position == 1 + 0j

    physical_object.move()
    assert physical_object.velocity == 2 + 0j
    assert physical_object.position == 3 + 0j
 
    physical_object.move()
    assert physical_object.velocity == 3 + 0j
    assert physical_object.position == 6 + 0j
