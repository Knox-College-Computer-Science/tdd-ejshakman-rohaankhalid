import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from src.calc import Calculator

@pytest.fixture(scope="module")
def calc():
    return Calculator()

def test_sine(calc):
    result = calc.sine(90)
    assert result == 1

def test_cosine(calc):
    result = calc.cosine(60)
    assert result == 0.5

def test_tangent(calc):
    result = calc.tangent(45)
    assert result == 1

def test_log(calc):
    result = calc.log10(100)
    assert result == 2


def test_log_error(calc):
    with pytest.raises(ValueError, match="logarithm for non-positive numbers is undefined"):
        calc.log10(0)

    with pytest.raises(ValueError, match="logarithm for non-positive numbers is undefined"):
        calc.log10(-10)
    
