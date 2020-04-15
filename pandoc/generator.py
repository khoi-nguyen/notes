from .algebra import *
from .analysis import *
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
    x = s.symbols('x')
    # a*x = b or x + a = b or x/a = b
    if level <= 3:
        a = randint(2, 5)
        b = randint(0, 9)
        cointoss = randint(0, 2)
        # Level 1 1,1, level 2 at most 1 negative, level 3 can have -1,-1
        sign_1 = (-1)**randint(0, 1) if level >= 2 else 1
        sign_2 = (-1)**randint(0, 1) if level >= 2 else 1
        if sign_1 == -1 and level == 2:
            sign_2 = 1

        if cointoss == 1:
            lhs, rhs = sign_1*a*x, sign_2*randint(0, 4)*a
        elif cointoss == 2:
            lhs, rhs = sign_1/a*x, sign_2*randint(0, 4)
        else:
            lhs, rhs = x + sign_1*a, sign_2*b + sign_1*a
    # a*x + b = c
    elif level <= 5:
        a = randint(2, 5)
        b = randint(1, 9)
        sign_1 = (-1)**randint(0, 1) if level == 5 else 1
        sign_2 = (-1)**randint(0, 1) if level == 5 else 1
        c = sign_2*b + randint(-9, 9)*a
        lhs, rhs = sign_1*a*x + sign_2*b, c
    # a*x + b = c*x + d (int solution)
    elif level <= 7:
        a = randint(2, 5)
        b = randint(1, 9)
        c = randint(1, 9)
        sign_1 = (-1)**randint(0, 1) if level == 7 else 1
        sign_2 = (-1)**randint(0, 1) if level == 7 else 1
        sign_3 = (-1)**randint(0, 1) if level == 7 else 1
        d = sign_2*b + randint(-9, 9)*(sign_1*a - sign_3*c)
        lhs, rhs = sign_1*a*x + sign_2*b, sign_3*c*x + d
    # a*x + b = c*x + d
    elif level <= 9:
        a = (-1)**randint(0,1)*randint(2, 9)
        b = (-1)**randint(0,1)*randint(1, 9)
        c = (-1)**randint(0,1)*randint(1, 9)
        d = (-1)**randint(0,1)*randint(1, 9)
        lhs, rhs = a*x + b, c*x + d
    return ('Solve',) + equation(str(s.simplify(lhs)), str(s.simplify(rhs)))

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
