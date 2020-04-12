from .algebra import *
from random import randint

import sympy as s

def generate_quadratic_equation():
    x1 = randint(-5, 5)
    x2 = randint(-5, 5)
    x = s.symbols('x')
    eq = s.expand((x - x1)*(x - x2))
    return equation(str(eq))
