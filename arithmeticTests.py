import calc
import unittest

class testAdd(unittest.TestCase):
    def test_add_pos(self):
        self.assertEqual(calc.add(1, 2), 3)

    def test_add_neg(self):
        self.assertEqual(calc.add(-1, -2), -3)

    def test_add_mix(self):
        self.assertEqual(calc.add(10, -5), 5)           #large pos + small neg
        self.assertEqual(calc.add(-8, 2), -6)           #large neg + small pos
        self.assertEqual(calc.add(5, -5), 0)            #self pos + self neg
        self.assertEqual(calc.add(-5, 5), 0)            #self neg + self pos

    def test_add_zero(self):
        self.assertEqual(calc.add(0, 0), 0)
        self.assertEqual(calc.add(2, 0), 2)             #pos + 0
        self.assertEqual(calc.add(-2, 0), -2)           #neg + 0

    def test_add_error(self):
        self.assertEqual(calc.add(2, 0), -2)           #neg + 0


class testSubtract(unittest.TestCase):
    def test_sub_pos(self):
        self.assertEqual(calc.subtract(5, 2), 3)        #large - small
        self.assertEqual(calc.subtract(3, 7), -4)       #small - large
        self.assertEqual(calc.subtract(5, 5), 0)        #self - self

    def test_sub_neg(self):
        self.assertEqual(calc.subtract(-3, -2), -1)     #large - small
        self.assertEqual(calc.subtract(-3, -3), 0)      #small - large
        self.assertEqual(calc.subtract(-3, -3), 0)      #self - self

    def test_sub_mix(self):
        self.assertEqual(calc.subtract(10, -5), 15)     #large pos - small neg
        self.assertEqual(calc.subtract(-8, 2), -10)     #large neg - small pos

    def test_sub_same(self):
        self.assertEqual(calc.subtract(10, 10), 0)      #pos
        self.assertEqual(calc.subtract(-5, -5), 0)      #neg
        self.assertEqual(calc.subtract(7, -7), 14)      #pos - neg
        self.assertEqual(calc.subtract(-3, 3), -6)      #neg - pos

    def test_sub_zero(self):
        self.assertEqual(calc.subtract(0, 0), 0)
        self.assertEqual(calc.subtract(5, 0), 5)        #pos - 0
        self.assertEqual(calc.subtract(0, 5), -5)       #0 - pos
        self.assertEqual(calc.subtract(-2, 0), -2)      #neg - 0
        self.assertEqual(calc.subtract(0, -4), 4)       #0 - neg

    def test_sub_error(self):
        self.assertEqual(calc.subtract(5, 2), -3)        #large - small

if __name__ == '__main__':
    unittest.main()