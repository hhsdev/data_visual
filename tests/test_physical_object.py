# _*_ coding: utf-8 _*_

from data_visual.physical_object import PhysicalObject
from data_visual.vec2 import Vec2

import pytest

@pytest.fixture
def physicalObject():
    return PhysicalObject(Vec2(0, 0))

def test_moveBy(physicalObject):
    physicalObject.moveBy(Vec2(2, 2))
    assert physicalObject.position == Vec2(2, 2)

    physicalObject.moveBy(Vec2(2, 2))
    assert physicalObject.position == Vec2(4, 4)

def test_linear_move(physicalObject):
    physicalObject.velocity = Vec2(1, 1)
    physicalObject.move()
    assert physicalObject.position == Vec2(1, 1)
    physicalObject.move()
    physicalObject.move()
    physicalObject.move()
    assert physicalObject.position == Vec2(4, 4)

def test_constant_accleration_move(physicalObject):
    physicalObject.acceleration = Vec2(1, 0)

    physicalObject.move()
    assert physicalObject.velocity == Vec2(1, 0)
    assert physicalObject.position == Vec2(1, 0)

    physicalObject.move()
    assert physicalObject.velocity == Vec2(2, 0)
    assert physicalObject.position == Vec2(3, 0)

    physicalObject.move()
    assert physicalObject.velocity == Vec2(3, 0)
    assert physicalObject.position == Vec2(6, 0)

