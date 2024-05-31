import pytest
import math
from src.calculator import Calculator

def test_sine():
    calc = Calculator()
    result = calc.sine(90)
    assert result == 1

def test_cosine():
    calc = Calculator()
    result = calc.cosine(60)
    assert result == 0.5

def test_tangent():
    calc = Calculator()
    result = calc.tangent(45)
    assert result == 1

def test_log():
    calc = Calculator()
    result = calc.log10(100)
    assert result == 2

def test_ln():
    calc = Calculator()
    result = calc.ln(1)
    assert result == 0
