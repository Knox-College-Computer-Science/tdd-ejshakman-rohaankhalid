import pytest
from src.logic import CalculatorLogic

@pytest.fixture(scope="module")
def calc():
    return CalculatorLogic()

def test_add(calc):
    assert calc.add(1, 2) == 3
    assert calc.add(-1, -2) == -3
    assert calc.add(10, -5) == 5
    assert calc.add(-8, 2) == -6
    assert calc.add(5, -5) == 0
    assert calc.add(-5, 5) == 0
    assert calc.add(0, 0) == 0
    assert calc.add(2, 0) == 2
    assert calc.add(-2, 0) == -2

def test_add_error(calc):
    with pytest.raises(AssertionError):
        assert calc.add(9, 1) == 6

def test_subtract(calc):
    assert calc.subtract(5, 2) == 3
    assert calc.subtract(3, 7) == -4
    assert calc.subtract(5, 5) == 0
    assert calc.subtract(-3, -2) == -1
    assert calc.subtract(-3, -3) == 0
    assert calc.subtract(10, -5) == 15
    assert calc.subtract(-8, 2) == -10
    assert calc.subtract(10, 10) == 0
    assert calc.subtract(-5, -5) == 0
    assert calc.subtract(7, -7) == 14
    assert calc.subtract(-3, 3) == -6
    assert calc.subtract(0, 0) == 0
    assert calc.subtract(5, 0) == 5
    assert calc.subtract(0, 5) == -5
    assert calc.subtract(-2, 0) == -2
    assert calc.subtract(0, -4) == 4

def test_subtract_error(calc):
    with pytest.raises(AssertionError):
        assert calc.subtract(9, 1) == 6

def test_multiply(calc):
    assert calc.multiply(-2, 3) == -6
    assert calc.multiply(3, 0) == 0

def test_divide(calc):
    assert calc.divide(3, 1) == 3
    assert calc.divide(6, -2) == -3

def test_divide_error(calc):
    with pytest.raises(ZeroDivisionError):
        calc.divide(12, 0)
