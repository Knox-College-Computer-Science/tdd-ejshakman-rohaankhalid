# tests/test_gui.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from tkinter import Tk
from src.calculator_gui import Calculator

@pytest.fixture
def gui():
    root = Tk()
    calc = Calculator(root)
    yield calc
    root.destroy()

# Display screen initialization
def test_display_initialization(gui):
    assert gui.get_display_text() == ""

# Display screen update
def test_display_update(gui):
    gui.press_button('1')
    gui.press_button('+')
    gui.press_button('2')
    
    assert gui.get_display_text() == "1+2"

# Numeric buttons
def test_numeric_buttons(gui):
    gui.press_button('3')
    gui.press_button('4')
    gui.press_button('5')

    assert gui.get_display_text() == "345"

# Operator buttons
def test_operator_buttons(gui):
    gui.press_button('3')
    gui.press_button('-')
    gui.press_button('1')
    gui.press_button('=')

    assert gui.get_display_text() == "2"

# Equal button
def test_equal_button(gui):
    gui.press_button('7')
    gui.press_button('-')
    gui.press_button('3')
    gui.press_button('=')

    assert gui.get_display_text() == "4"

# Clear all button
def test_clear_all_button(gui):
    gui.press_button('6')
    gui.press_button('7')
    gui.press_button('C')

    assert gui.get_display_text() == ""

# Clear button
def test_clear_button(gui):
    gui.press_button('9')
    gui.press_button('0')
    gui.press_button('CE')

    assert gui.get_display_text() == "9"