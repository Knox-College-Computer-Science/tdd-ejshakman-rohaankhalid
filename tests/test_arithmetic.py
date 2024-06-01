import unittest
from src.calc import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, -2), -3)
        self.assertEqual(self.calc.add(10, -5), 5)
        self.assertEqual(self.calc.add(-8, 2), -6)
        self.assertEqual(self.calc.add(5, -5), 0)
        self.assertEqual(self.calc.add(-5, 5), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(2, 0), 2)
        self.assertEqual(self.calc.add(-2, 0), -2)

    def test_add_error(self):
        with self.assertRaises(AssertionError):
            self.assertEqual(self.calc.add(9, 1), 6)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(3, 7), -4)
        self.assertEqual(self.calc.subtract(5, 5), 0)
        self.assertEqual(self.calc.subtract(-3, -2), -1)
        self.assertEqual(self.calc.subtract(-3, -3), 0)
        self.assertEqual(self.calc.subtract(10, -5), 15)
        self.assertEqual(self.calc.subtract(-8, 2), -10)
        self.assertEqual(self.calc.subtract(10, 10), 0)
        self.assertEqual(self.calc.subtract(-5, -5), 0)
        self.assertEqual(self.calc.subtract(7, -7), 14)
        self.assertEqual(self.calc.subtract(-3, 3), -6)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-2, 0), -2)
        self.assertEqual(self.calc.subtract(0, -4), 4)

    def test_subtract_error(self):
        with self.assertRaises(AssertionError):
            self.assertEqual(self.calc.subtract(9, 1), 6)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(3, 0), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(3, 1), 3)
        self.assertEqual(self.calc.divide(6, -2), -3)

    def test_divide_error(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(12, 0)

if __name__ == '__main__':
    unittest.main()