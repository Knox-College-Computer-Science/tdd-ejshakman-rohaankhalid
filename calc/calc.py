import math

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("division by zero")
        return a / b
    
    def sine(self, x):
        return round(math.sin(math.radians(x)), 6)
    
    def cosine(self, x):
        return round(math.cos(math.radians(x)), 6)
    
    def tangent(self, x):
        return round(math.tan(math.radians(x)), 6)
    
    def log10(self, x):
        if x <= 0:
            raise ValueError("logarithm for non-positive numbers is undefined")
        return round(math.log10(x), 6)
    
    def ln(self, x):
        if x <= 0:
            raise ValueError("natural logarithm for non-positive numbers is undefined")
        return round(math.log(x), 6)
