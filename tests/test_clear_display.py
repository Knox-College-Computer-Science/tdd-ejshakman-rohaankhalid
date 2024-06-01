# tests/test_clear_display.py
import pytest
from src.calc import Calculator

@pytest.fixture(scope="module")
def calc():
    return Calculator()

def test_clear(calc):
    calc.clear()
    assert calc.display == ""
