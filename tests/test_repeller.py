# _*_ coding: utf-8 _*_

import pytest
from data_visual.repeller import Repeller
from data_visual.physical_object import PhysicalObject
from data_visual.vec2 import Vec2

@pytest.fixture
def repeller():
    return Repeller(1.0)

def test_actOn(repeller):
    assert repeller.intensity == 1.0
    stone = PhysicalObject()
    stone.position = Vec2(1, 0)
    repeller.actOn(stone)
    assert stone.acceleration == Vec2(1.0, 0)

