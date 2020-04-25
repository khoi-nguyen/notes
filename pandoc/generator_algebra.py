from .algebra import *
from random import randint, choice

import sympy as s

def generate_circle_equation(level):
    """Radius/center from circle equation"""
    info = 'center' if randint(0, 1) else 'radius'
    lower_bound = -9 if level >= 3 else 0
    m = 1 if level <= 8 else randint(1, 2)
    a = randint(m*lower_bound, m*9)
    b = randint(m*lower_bound, m*9)
    x, y = s.symbols('x y')
    lhs = (m*x - a)**2 + (m*y - b)**2
    rhs = m**2*randint(1, 9)**2
    if level >= 5:
        lhs = s.expand(lhs)
    if level >= 6:
        offset = randint(-25, 25)
        lhs += offset
        rhs += offset
    return (f'Find the {info} of the circle whose equation is',) + circle_equation(info, lhs, rhs)

def generate_complete_square(level):
    """Completing the square"""
    x = s.symbols('x')
    a, d, k = 1, 1, 0
    if level <= 2:
        h = randint(0, 9)
    elif level <= 4:
        h = randint(0, 9)
        k = randint(0, 9)
    elif level <= 6:
        h = randint(-9, 9)
        k = randint(-9, 9)
    else:
        a = (-1)**randint(0, 1)*randint(1, 3*d)
        h = randint(-9*d, 9*d)
        k = randint(-9*d, 9*d)
        if level >= 8:
            d = randint(1, 2 if d < 9 else 3)
    eq = s.expand((a*(x + h)**2 + k)/d)
    return ('Complete the square',) + complete_square(eq)

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
        b = randint(1, 9)
        c = randint(1, 9)
        sign_1 = (-1)**randint(0, 1) if level == 7 else 1
        sign_2 = (-1)**randint(0, 1) if level == 7 else 1
        sign_3 = (-1)**randint(0, 1) if level == 7 else 1
        a = sign_1*sign_3*c + (-1)**randint(0, 1)*randint(1, 9)
        d = sign_2*b + randint(-9, 9)*(sign_1*a - sign_3*c)
        lhs, rhs = sign_1*a*x + sign_2*b, sign_3*c*x + d
    # a*x + b = c*x + d
    elif level <= 9:
        b = (-1)**randint(0,1)*randint(1, 9)
        c = (-1)**randint(0,1)*randint(1, 9)
        d = (-1)**randint(0,1)*randint(1, 9)
        sign_1 = (-1)**randint(0, 1)
        sign_2 = (-1)**randint(0, 1)
        sign_3 = (-1)**randint(0, 1)
        a = sign_1*sign_3*c + (-1)**randint(0, 1)*randint(1, 9)
        lhs, rhs = sign_1*a*x + sign_2*b, sign_3*c*x + d
    return ('Solve',) + equation(str(s.simplify(lhs)), str(s.simplify(rhs)))

def generate_expindex(level):
    """Expanding powers"""
    base = randint(2, 9)
    power = randint(2, 5)
    return ('Expand the power',) + expindex(base, power)

def generate_multindex(level):
    """Multiply Indices"""
    # a**m * a**n where a is an integer
    if level <= 2:
        base = randint(2, 5)
        power_1 = randint(1, 3 if level == 1 else 5)
        power_2 = randint(1, 3 if level == 1 else 5)
    # x**m * x**n
    elif level <= 6:
        variables = ['a', 'b', 'c', 'm', 'n', 'x', 'y', 'z']
        base = choice(variables)
        power_1 = randint(1 if level <= 4 else -9, 5 if level == 3 else 9)
        power_2 = randint(1 if level <= 4 else -9, 5 if level == 3 else 9)
    # y**m * y**n where y can be integer or variable
    elif level <= 8:
        base = choice(['a', 'b', 'c', 'm', 'n', 'x', 'y', 'z'] + list(range(2, 10)))
        power_1 = randint(-9, 9)
        power_2 = randint(-9, 9)
    # a**m * a**n -5 ≤ a ≤ -2
    else:
        variables = ['a', 'b', 'c', 'm', 'n', 'x', 'y', 'z']
        base = choice(variables)
        base_1 = f'(-{base})' if randint(0, 1) else base
        base_2 = f'(-{base})' if randint(0, 1) else base
        power_1 = randint(-9, 9)
        power_2 = randint(-9, 9)
    # Answers for integer or variable base
    if isinstance(base, int):
        return ('Simplify the following',) + mult(f'a^{power_1}', f'a^{power_2}', a=base)
    elif level == 9:
        return ('Simplify the following',) + mult(f'{base_1}^{power_1}', f'{base_2}^{power_2}')
    else:
        return ('Simplify the following',) + mult(f'{base}^{power_1}', f'{base}^{power_2}')

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

def generate_stf(level):
    """Standard form"""
    if level <= 3:
        x = randint(1, 9)
        ranges = {1: (1, 3), 2: (-3, -1), 3: (-3, 3)}
        power = randint(*ranges[level])
    elif level <= 6:
        x = randint(11, 99)/10
        ranges = {4: (1, 5), 5: (-5, -1), 6: (-5, 5)}
        power = randint(*ranges[level])
    else:
        number_1 = randint(101, 9999)
        x = number_1/(100 if number_1 < 1000 else 1000)
        power = randint(-7, 7)
    return ('Convert to standard form',) + stf(x*10**power)

def generate_stf2dec(level):
    """Standard form to ordinary"""
    return ('Convert to an ordinary number',) + generate_stf(level)[2:0:-1]
