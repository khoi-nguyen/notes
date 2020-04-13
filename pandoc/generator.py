from .algebra import *
from random import randint

import sympy as s

def generate_multindex(level):
    """Multiply Indices"""
    base = randint(1, 9)
    power_1 = randint(0, 9)
    power_2 = randint(0, 9)
    return ('Multiply Index',) + mult(f'a^{power_1}', f'a^{power_2}', a=base)

def generate_stf(level):
    """Standard form"""
    x = randint(1, 99999)
    power = -len(str(x)) + randint(-2, 7)
    return ('Convert to standard form',) + stf(round(x*10**power, 4))

def generate_expindex(level):
    """Expanding powers"""
    base = randint(2, 9)
    power = randint(2, 5)
    return ('Expand the power',) + expindex(base, power)

def generate_equation(level):
    """Linear equation"""
    a = (-1)**randint(0, 1)*randint(1, 5)
    b = randint(-5, 5)
    c = randint(-5, 5)
    x = s.symbols('x')
    return ('Solve',) + equation(f'{str(a * x + b)} = {c}')

def generate_quadratic_equation(level):
    """Quadratic equation"""
    x = s.symbols('x')
    # x^2 = square number
    if level < 3:
        square_number = randint(0, 9)**2
        n = (-1)**randint(0, 1) * randint(0, square_number)
        lhs, rhs = x**2 + n, n + square_number
    # a*x(x - x1) = 0
    elif level == 4:
        a = (-1)**randint(0, 1) * randint(1, 4)
        c = randint(-9, 9)
        lhs, rhs = s.expand(a * x * (x - c)), 0
    # (a*x - x1)*(x - x2) = 0, with a = 1 for level 5, with rhs for >= 7
    elif level < 8:
        a = (-1)**randint(0, 1) * randint(1, 3) if level > 5 else 1
        x1, x2 = randint(-5, 5), randint(-5, 5)
        lhs, rhs = s.expand((a*x - x1)*(x - x2)), 0
        if level == 7:
            b, c = randint(-9, 9), randint(-9, 9)
            lhs = lhs + b*x + c
            rhs = b*x + c
    # Only require that discriminant is nonnegative
    else:
        a = (-1)**randint(0, 1) * randint(1, 4)
        b, Delta = randint(-9, 9), randint(0, 9)
        d, e = randint(-9, 9), randint(-9, 9)
        lhs = s.expand(a* (x - (-b + s.sqrt(Delta))/(2*a)) * (x - (-b - s.sqrt(Delta))/(2*a)) + d*x + e)
        rhs = d*x + e
    return ('Solve',) + equation(str(lhs), str(rhs))
