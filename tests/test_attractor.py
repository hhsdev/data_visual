# _*_ coding: utf-8 _*_

import pytest
from pytest import approx

from data_visual.attractor import Attractor
from data_visual.physical_object import PhysicalObject
from data_visual.vec2 import Vec2


allInputsSetToOne = {
        'attractor': {
            'intensity': 1,
            'position': Vec2(0, 0),
        },
        'receiver': {
            'mass': 1,
            'position': Vec2(1, 0),
        },

        'result': {
            'force': Vec2(-1, 0),
        }
}

allInputsSetToZero = {
        'attractor': {
            'intensity': 0,
            'position': Vec2(0, 0),
        },
        'receiver': {
            'mass': 0,
            'position': Vec2(0, 0),
        },

        'result': {
            'force': Vec2(0, 0)
        }
} 

randomTestCase1 = {
        'attractor': {
            'intensity': 1.23,
            'position': Vec2(1.2, 3.5),
        },
        'receiver': {
            'mass': 23.4,
            'position': Vec2(1.3, 6.4),
        },

        'result': {
            'force': Vec2(-1.178020e-1, -3.416259)
        }
}

@pytest.mark.parametrize('fixture', [
    allInputsSetToOne,
    allInputsSetToZero,
    randomTestCase1
])
def testActOn(fixture):
    attractor = Attractor(
            fixture['attractor']['intensity'],
            fixture['attractor']['position'])

    objectToMove = PhysicalObject(
            fixture['receiver']['position'],
            fixture['receiver']['mass'])
    attractor.actOn(objectToMove)
    
    expectedForce = fixture['result']['force']
    assert objectToMove.force.x == approx(expectedForce.x)
    assert objectToMove.force.y == approx(expectedForce.y)

