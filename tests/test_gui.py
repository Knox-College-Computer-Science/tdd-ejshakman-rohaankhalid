import pytest
from tkinter import Tk
from src.gui import CalculatorGUI
from src.logic import CalculatorLogic

@pytest.fixture
def gui():
    root = Tk()
    calc = CalculatorGUI(root)
    yield calc
    root.destroy()

# Display screen initialization
def test_display_initialization(gui):
    assert gui.current_input() == ""

# Display screen update
def test_display_update(gui):
    gui.on_button_click('1')
    gui.on_button_click('+')
    gui.on_button_click('2')
    
    assert gui.current_input() == "1+2"

# Numeric buttons
def test_numeric_buttons(gui):
    gui.on_button_click('3')
    gui.on_button_click('4')
    gui.on_button_click('5')

    assert gui.current_input() == "345"

# Operator buttons
def test_operator_buttons(gui):
    gui.on_button_click('3')
    gui.on_button_click('-')
    gui.on_button_click('1')
    gui.on_button_click('=')

    assert gui.current_input() == "2"

# Equal button
def test_equal_button(gui):
    gui.on_button_click('7')
    gui.on_button_click('-')
    gui.on_button_click('3')
    gui.on_button_click('=')

    assert gui.current_input() == "4"

# Clear all button
def test_clear_all_button(gui):
    gui.on_button_click('6')
    gui.on_button_click('7')
    gui.on_button_click('C')

    assert gui.current_input() == ""

# Clear button
def test_clear_button(gui):
    gui.on_button_click('9')
    gui.on_button_click('0')
    gui.on_button_click('CE')

    assert gui.current_input() == "9"
    