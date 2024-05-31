import pytest
from src.calculator import Calculator

def setup_function():
    global calc
    calc = Calculator()

def test_sine():
    result = calc.sine(90)
    assert result == 1

def test_cosine():
    result = calc.cosine(60)
    assert result == 0.5

def test_tangent():
    result = calc.tangent(45)
    assert result == 1

def test_log():
    result = calc.log10(100)
    assert result == 2

def test_ln():
    result = calc.ln(1)
    assert result == 0
