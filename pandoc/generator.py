from .algebra import *
from random import randint

import sympy as s

def generate_equation():
    """Linear equation"""
    a = (-1)**randint(0, 1)*randint(1, 5)
    b = randint(-5, 5)
    c = randint(-5, 5)
    x = s.symbols('x')
    return equation(f'{str(a * x + b)} = {c}')

def generate_quadratic_equation():
    """Quadratic equation"""
    x1 = randint(-5, 5)
    x2 = randint(-5, 5)
    x = s.symbols('x')
    eq = s.expand((x - x1)*(x - x2))
    return equation(str(eq))
