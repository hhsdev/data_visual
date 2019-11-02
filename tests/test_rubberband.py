# _*_ coding: utf-8 _*_
import pytest
from pytest import approx
from data_visual.rubberband import Rubberband

test_case1 = {
    'intensity': 1,
    'a': {
        'position': 0j,
        'velocity': 0j,
        'force': 1 + 0j
    },
    'b': {
        'position': 1 + 0j,
        'velocity': 0j,
        'force': -1 + 0j
    }
}

test_case2 = {
    'intensity': 244.35,
    'a': {
        'position': 1.2 + 0.435j,
        'velocity': 0j,
        'force': 4.3983e2 + 1.0496421e5j
    },
    'b': {
        'position': 3 + 430j,
        'velocity': 0j,
        'force': -4.3983e2 + -1.0496421e5j
    }
}


class MockObject(object):
    def __init__(self, label, position, velocity):
        self.label = label
        self.position = position
        self.velocity = velocity
        self.force = 0j
    
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
    
    assert object_a.force == approx(fixture['a']['force'])
    assert object_b.force == approx(fixture['b']['force'])
