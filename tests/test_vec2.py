from data_visual.vec2 import Vec2
from math import hypot
import pytest

@pytest.fixture
def vecOne():
    return Vec2(1, 2)

@pytest.fixture
def vecTwo():
    return Vec2(3, 4)

def test_init(vecOne):
    assert vecOne.x == 1
    assert vecOne.y == 2

def test_compare():
    assert Vec2(1, 2) == Vec2(1, 2)
    assert Vec2(1, 2) != Vec2(3, 4)

    assert Vec2(1, 2) != Vec2(1, 4)
    assert Vec2(1, 2) != Vec2(3, 2)

def test_add(vecOne, vecTwo):
    twoVecAdd =  vecOne + vecTwo
    assert twoVecAdd.x == vecOne.x + vecTwo.x
    assert twoVecAdd.y == vecOne.y + vecTwo.y
    
    scalerAdd = vecOne + 2
    assert scalerAdd.x == vecOne.x + 2
    assert scalerAdd.y == vecOne.y + 2

    oldVecOne = Vec2(vecOne.x, vecOne.y)
    vecOne += vecTwo
    assert vecOne.x == oldVecOne.x + vecTwo.x
    assert vecOne.y == oldVecOne.y + vecTwo.y

    oldVecTwo = Vec2(vecTwo.x, vecTwo.y)
    vecTwo += 2
    assert vecTwo.x == oldVecTwo.x + 2
    assert vecTwo.y == oldVecTwo.y + 2

def test_minus(vecOne, vecTwo):
    twoVecSubtract =  vecOne - vecTwo
    assert twoVecSubtract.x == vecOne.x - vecTwo.x
    assert twoVecSubtract.y == vecOne.y - vecTwo.y
    
    scalerSubtract = vecOne - 2
    assert scalerSubtract.x == vecOne.x - 2
    assert scalerSubtract.y == vecOne.y - 2

    oldVecOne = Vec2(vecOne.x, vecOne.y)
    vecOne -= vecTwo
    assert vecOne.x == oldVecOne.x - vecTwo.x
    assert vecOne.y == oldVecOne.y - vecTwo.y

    oldVecTwo = Vec2(vecTwo.x, vecTwo.y)
    vecTwo -= 2
    assert vecTwo.x == oldVecTwo.x - 2
    assert vecTwo.y == oldVecTwo.y - 2

def test_abs(vecOne, vecTwo):
    assert abs(vecOne) == hypot(vecOne.x, vecOne.y)
    assert abs(vecTwo) == hypot(vecTwo.x, vecTwo.y)

def test_multiply(vecOne, vecTwo):
    vecMultiply = vecOne * 2
    assert vecMultiply.x == vecOne.x * 2
    assert vecMultiply.y == vecOne.y * 2

    vecReverseMultiply = 2 * vecOne
    assert vecReverseMultiply.x == vecOne.x * 2
    assert vecReverseMultiply.y == vecOne.y * 2

    oldVecOne = Vec2(vecOne.x, vecOne.y)
    vecOne *= 2
    assert vecOne.x == oldVecOne.x * 2
    assert vecOne.y == oldVecOne.y * 2

def test_divide(vecOne, vecTwo):
    vecDivide = vecOne / 2
    assert vecDivide.x == vecOne.x / 2
    assert vecDivide.y == vecOne.y / 2

    vecReverseDivide = 2 / vecOne
    assert vecReverseDivide.x == vecOne.x / 2
    assert vecReverseDivide.y == vecOne.y / 2

    oldVecOne = Vec2(vecOne.x, vecOne.y)
    vecOne /= 2
    assert vecOne.x == oldVecOne.x / 2
    assert vecOne.y == oldVecOne.y / 2

