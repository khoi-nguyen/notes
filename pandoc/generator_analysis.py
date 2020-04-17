from .analysis import *
from random import randint

import sympy as s

def generate_find_linear_equation(level):
    """Linear equation from two points"""
    x = s.symbols('x')
    # y = ax or y = x + b with one easy point
    if level <= 3:
        cointoss = randint(0, 1)
        sign = (-1) ** randint(0, 1) if level == 3 else 1
        if cointoss:
            eq = sign*x + randint(-9, 9)
            x1 = 0
        else:
            eq = randint(1, 4) * sign * x
            x1 = 1
        x2 = randint(2, 4)
    # y = a*x + b, x's in order and positive
    elif level <= 5:
        a = randint(0, 5) if level == 4 else randint(-5, 5)
        eq = a*x + randint(-9, 9)
        x1 = randint(0, 3)
        x2 = x1 + randint(1, 3)
    # y = a*x + b with integer coefficients, no restriction on x's
    elif level <= 7:
        eq = randint(-5, 5)*x + randint(-9, 9)
        x1 = randint(-3, 3)
        x2 = x1 + (-1)**randint(0, 1) * randint(1, 5)
    # Allow halves
    else:
        eq = (randint(-10, 10)*x + randint(-20, 20))
        x1 = randint(-10, 10)
        x2 = x1 + (-1)**randint(0, 1) * randint(1, 10)

    y1 = eq.subs(x, x1)
    y2 = eq.subs(x, x2)

    # After substitutions to avoid floats
    if level >= 8:
        y1 = f'{y1}/2'
        y2 = f'{y2}/2'

    text = ('Find the equation of the line passing through',)
    return text + line_equation(x1, y1, x2, y2)
