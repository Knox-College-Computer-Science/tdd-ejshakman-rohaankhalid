# tests/test_clear_display.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from src.calc import Calculator

@pytest.fixture(scope="module")
def calc():
    return Calculator()

def test_clear(calc):
    calc.clear()
    assert calc.display == ""
