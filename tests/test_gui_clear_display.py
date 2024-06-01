# tests/test_gui_clear_display.py
import pytest
from tkinter import Tk
from src.calculatorGui import Calculator

@pytest.fixture
def gui_calc():
    root = Tk()
    calc = Calculator(root)
    yield calc
    root.destroy()

def test_gui_clear_display(gui_calc):
    gui_calc.entry.insert(0, "5 + 3")
    gui_calc.on_button_click("C")
    assert gui_calc.entry.get() == ""
