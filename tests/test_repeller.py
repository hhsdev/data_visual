# _*_ coding: utf-8 _*_

import pytest
from pytest import approx

from data_visual.repeller import Repeller
from data_visual.physical_object import PhysicalObject
from data_visual.vec2 import Vec2


allInputsSetToOne = {
        'repeller': {
            'intensity': 1,
            'position': Vec2(0, 0),
        },
        'receiver': {
            'mass': 1,
            'position': Vec2(1, 0),
        },

        'result': {
            'force': Vec2(1, 0),
        }
}

allInputsSetToZero = {
        'repeller': {
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
        'repeller': {
            'intensity': 1.23,
            'position': Vec2(1.2, 3.5),
        },
        'receiver': {
            'mass': 23.4,
            'position': Vec2(1.3, 6.4),
        },

        'result': {
            'force': Vec2(1.178020e-1, 3.416259)
        }
}

@pytest.mark.parametrize('fixture', [
    randomTestCase1

])
def testActOn(fixture):
    repeller = Repeller(
            fixture['repeller']['intensity'],
            fixture['repeller']['position'])

    objectToMove = PhysicalObject(
            fixture['receiver']['position'],
            fixture['receiver']['mass'])
    repeller.actOn(objectToMove)
    
    expectedForce = fixture['result']['force']
    assert objectToMove.force.x == approx(expectedForce.x)
    assert objectToMove.force.y == approx(expectedForce.y)

