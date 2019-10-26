# _*_ coding: utf-8 _*_
import pytest
from pytest import approx
from data_visual.vec2 import Vec2
from data_visual.rubberband import Rubberband

test_case1 = {
    'intensity': 1,
    'a': {
        'position': Vec2(0, 0),
        'velocity': Vec2(0, 0),
        'force': Vec2(1, 0)
    },
    'b': {
        'position': Vec2(1, 0),
        'velocity': Vec2(0, 0),
        'force': Vec2(-1, 0)
    }
}

test_case2 = {
    'intensity': 244.35,
    'a': {
        'position': Vec2(1.2, 0.435),
        'velocity': Vec2(0, 0),
        'force': Vec2(439.83, 104964.20775)
    },
    'b': {
        'position': Vec2(3, 430),
        'velocity': Vec2(0, 0),
        'force': Vec2(-439.83, -104964.20775)
    }
}


class MockObject(object):
    def __init__(self, label, position, velocity):
        self.label = label
        self.position = position
        self.velocity = velocity
        self.force = Vec2()
    
    def __eq__(self, other):
        return self.label == other.label
    
    def __neq__(self, other):
        return self.label != other.label

@pytest.mark.parametrize('fixture', [
    test_case1,
    test_case2
])
def test_act_on(fixture):
    object_a = MockObject(
            'a', fixture['a']['position'], fixture['a']['velocity'])
    object_b = MockObject(
            'b', fixture['b']['position'], fixture['b']['velocity'])

    rubberband = Rubberband(
            object_a, object_b, fixture['intensity'])

    rubberband.act_on(object_a)
    rubberband.act_on(object_b)

    assert object_a.force.x == approx(fixture['a']['force'].x)
    assert object_a.force.y == approx(fixture['a']['force'].y)

    assert object_b.force.x == approx(fixture['b']['force'].x)
    assert object_b.force.y == approx(fixture['b']['force'].y)
