from solver.algebra import (
    circle_equation,
    complete_square,
    div,
    equation,
    expindex,
    mult,
    stf,
    stfmult,
    stfadd,
    stfdiv,
    stfsub,
)
from math import gcd
from generator.helpers import pick
from random import randint, choice

from sympy import (
    Abs,
    expand as Expand,
    simplify as Simplify,
    nsimplify,
    sign,
    sqrt,
    symbols,
)


def condition_frac(ascending_order=False):
    if ascending_order:
        return lambda a, b: a < b and gcd(a, b) == 1
    else:
        return lambda a, b: gcd(a, b) == 1


def generate_circle_equation(level):
    """Radius/center from circle equation"""
    # Generating a random equation in canonical form
    (a, b, r, offset) = pick(
        {
            1: ([0, 9], [0, 9], [1, 9], [0, 0]),
            3: ([-9, 9], [-9, 9], [1, 9], [0, 0]),
            5: ([-9, 9], [-9, 9], [1, 9], [-25, 25]),
            8: ([-9, 9, 0.5], [-9, 9, 0.5], [1, 9, 0.5], [-25, 25, 0.5]),
        },
        level,
    )
    x, y = symbols("x y")
    lhs = nsimplify((x - a) ** 2 + (y - b) ** 2 + offset)
    rhs = nsimplify(r ** 2 + offset)

    # Minor transformations for higher levels
    if level >= 5:
        lhs = Expand(lhs)

    info = "center" if randint(0, 1) else "radius"
    return (f"Find the {info} of the circle whose equation is",) + circle_equation(
        info, lhs, rhs
    )


def generate_complete_square(level):
    """Completing the square"""
    (a, h, k) = pick(
        {
            1: ([1, 1], [0, 9], [0, 0]),
            3: ([1, 1], [0, 9], [0, 9]),
            5: ([1, 1], [0, 9], [-9, 9]),
            6: ([1, 1], [-9, 9], [-9, 9]),
            7: ([-3, 3], [-9, 9], [-9, 9], lambda a, h, k: a != 0),
            8: ([-3, 3, 0.5], [-9, 9, 0.5], [-9, 9, 0.5], lambda a, h, k: a != 0),
        },
        level,
    )
    x = symbols("x")
    eq = nsimplify(Expand(a * (x + h) ** 2 + k))
    return ("Complete the square",) + complete_square(eq)


def generate_equation(level):
    """Linear equation"""
    x = symbols("x")
    # a*x = b or x + a = b or x/a = b
    if level <= 3:
        a = randint(2, 5)
        b = randint(0, 9)
        cointoss = randint(0, 2)
        # Level 1 1,1, level 2 at most 1 negative, level 3 can have -1,-1
        sign_1 = (-1) ** randint(0, 1) if level >= 2 else 1
        sign_2 = (-1) ** randint(0, 1) if level >= 2 else 1
        if sign_1 == -1 and level == 2:
            sign_2 = 1

        if cointoss == 1:
            lhs, rhs = sign_1 * a * x, sign_2 * randint(0, 4) * a
        elif cointoss == 2:
            lhs, rhs = sign_1 / a * x, sign_2 * randint(0, 4)
        else:
            lhs, rhs = x + sign_1 * a, sign_2 * b + sign_1 * a
    # a*x + b = c
    elif level <= 5:
        a = randint(2, 5)
        b = randint(1, 9)
        sign_1 = (-1) ** randint(0, 1) if level == 5 else 1
        sign_2 = (-1) ** randint(0, 1) if level == 5 else 1
        c = sign_2 * b + randint(-9, 9) * a
        lhs, rhs = sign_1 * a * x + sign_2 * b, c
    # a*x + b = c*x + d (int solution)
    elif level <= 7:
        b = randint(1, 9)
        c = randint(1, 9)
        sign_1 = (-1) ** randint(0, 1) if level == 7 else 1
        sign_2 = (-1) ** randint(0, 1) if level == 7 else 1
        sign_3 = (-1) ** randint(0, 1) if level == 7 else 1
        a = sign_1 * sign_3 * c + (-1) ** randint(0, 1) * randint(1, 9)
        d = sign_2 * b + randint(-9, 9) * (sign_1 * a - sign_3 * c)
        lhs, rhs = sign_1 * a * x + sign_2 * b, sign_3 * c * x + d
    # a*x + b = c*x + d
    elif level <= 9:
        b = (-1) ** randint(0, 1) * randint(1, 9)
        c = (-1) ** randint(0, 1) * randint(1, 9)
        d = (-1) ** randint(0, 1) * randint(1, 9)
        sign_1 = (-1) ** randint(0, 1)
        sign_2 = (-1) ** randint(0, 1)
        sign_3 = (-1) ** randint(0, 1)
        a = sign_1 * sign_3 * c + (-1) ** randint(0, 1) * randint(1, 9)
        lhs, rhs = sign_1 * a * x + sign_2 * b, sign_3 * c * x + d
    return ("Solve",) + equation(str(Simplify(lhs)), str(Simplify(rhs)))


def generate_expindex(level):
    """Expanding powers"""
    base = randint(2, 9)
    power = randint(2, 5)
    return ("Expand the power",) + expindex(base, power)


def generate_multindex(level):
    """Multiply Indices"""
    # a**m * a**n where a is an integer
    if level <= 2:
        base = randint(2, 5)
        power_1 = randint(1, 3 if level == 1 else 5)
        power_2 = randint(1, 3 if level == 1 else 5)
    # x**m * x**n
    elif level <= 6:
        variables = ["a", "b", "c", "m", "n", "x", "y", "z"]
        base = choice(variables)
        power_1 = randint(1 if level <= 4 else -9, 5 if level == 3 else 9)
        power_2 = randint(1 if level <= 4 else -9, 5 if level == 3 else 9)
    # y**m * y**n where y can be integer or variable
    elif level <= 8:
        base = choice(["a", "b", "c", "m", "n", "x", "y", "z"] + list(range(2, 10)))
        power_1 = randint(-9, 9)
        power_2 = randint(-9, 9)
    # a**m * a**n -5 ≤ a ≤ -2
    else:
        variables = ["a", "b", "c", "m", "n", "x", "y", "z"]
        base = choice(variables)
        base_1 = f"(-{base})" if randint(0, 1) else base
        base_2 = f"(-{base})" if randint(0, 1) else base
        power_1 = randint(-9, 9)
        power_2 = randint(-9, 9)
    # Answers for integer or variable base
    if isinstance(base, int):
        return ("Simplify the following",) + mult(
            f"a^{power_1}", f"a^{power_2}", a=base
        )
    elif level == 9:
        return ("Simplify the following",) + mult(
            f"{base_1}^{power_1}", f"{base_2}^{power_2}"
        )
    else:
        return ("Simplify the following",) + mult(
            f"{base}^{power_1}", f"{base}^{power_2}"
        )


def generate_quadratic_equation(level):
    """Quadratic equation"""
    # Picking coefficients
    (a, u, v) = pick(
        {  # (a x - u) (x - v)
            1: ([1, 1], [-9, 9], [-9, 9], lambda a, u, v: u == -v),  # x^2 = uv
            3: ([-4, 4], [0, 0], [-9, 9], lambda a, u, v: a != 0),  # a x (x - v)
            5: ([1, 1], [-5, 5], [-5, 5]),  # (x - u) (x - v)
            6: ([-3, 3], [-5, 5], [-5, 5], lambda a, u, v: a != 0),  # a (x - u) (x - v)
        },
        level,
    )
    (d, e) = pick(
        {1: ([0, 0], [-30, 30]), 3: ([0, 0], [0, 0]), 7: ([-9, 9], [-9, 9])}, level
    )

    # Add surds for higher levels
    if level >= 8:
        u = u if randint(0, 3) else sign(u) * sqrt(Abs(u))
        v = v if randint(0, 3) else sign(v) * sqrt(Abs(v))

    x = symbols("x")
    lhs, rhs = Expand(a * (x - u) * (x - v)) + d * x + e, d * x + e
    return ("Solve",) + equation(str(lhs), str(rhs))


def generate_stf(level):
    """Standard form"""
    x = pick({1: [1, 9], 4: [1, 10, 0.1], 7: [1.01, 9.99, 0.01]}, level)
    power = pick({1: [1, 3], 3: [-3, -3], 5: [-5, 5], 7: [-5, 7]}, level)
    return ("Convert to standard form",) + stf(x * 10 ** power)


def generate_stfmult(level):
    """Multiply standard form"""
    powers_constraints = {
        1: [1, 3],
        3: [-3, -3],
        5: [-5, 5],
        7: [-5, 7],
    }
    bases_constraints = {
        1: ([1, 9], [1, 9], lambda x, y: x * y < 10),
        3: ([1, 9], [1, 9]),
        5: ([1, 9], [1.1, 9.9, 0.1]),
        7: ([1, 9], [1.01, 9.99, 0.01]),
    }

    (x, y) = pick(bases_constraints, level)
    power_1 = pick(powers_constraints, level)
    power_2 = pick(powers_constraints, level)
    return ("Work out and leave in standard form",) + stfmult(
        x * 10 ** power_1, y * 10 ** power_2
    )


def generate_stfadd(level):
    """Add standard form"""
    (x, y) = pick(
        {
            1: ([1, 9], [1, 9], lambda x, y: x + y < 10),
            3: ([1, 9], [1, 9]),
            5: ([1, 9], [1.1, 9.9, 0.1]),
            7: ([1, 9], [1.01, 9.99, 0.01]),
        },
        level,
    )
    bound_distance = lambda C: lambda p1, p2: Abs(p1 - p2) <= C
    powers_constraints = {
        1: ([1, 5], [1, 5], bound_distance(0)),
        3: ([-3, 3], [1, 5], bound_distance(1)),
        5: ([-5, 5], [1, 5], bound_distance(2)),
        7: ([-5, 7], [1, 5], bound_distance(5)),
    }

    (p1, p2) = pick(powers_constraints, level)
    return ("Work out and leave in standard form",) + stfadd(x * 10 ** p1, y * 10 ** p2)


def generate_stfdiv(level):
    """Divide standard form"""
    (x, y) = pick(
        {
            1: ([1, 9], [1, 9], lambda x, y: x / y < 10 and x % y == 0),
            3: ([1, 9], [1, 9], lambda x, y: x % y == 0),
            5: ([1.1, 9.9, 0.1], [1, 9], lambda x, y: 10 * x % y == 0),
            7: ([1.1, 9.9, 0.1], [1.2, 9.8, 0.2], lambda x, y: 100 * x % (10 * y) == 0),
        },
        level,
    )
    powers_constraints = {
        1: [1, 3],
        3: [-3, 3],
        5: [-5, 5],
        7: [-5, 7],
    }
    power_1 = pick(powers_constraints, level)
    power_2 = pick(powers_constraints, level)
    return ("Work out and leave in standard form",) + stfdiv(
        x * 10 ** power_1, y * 10 ** power_2
    )


def generate_stfsub(level):
    """Subtract standard form"""
    (x, y) = pick(
        {
            1: ([1, 9], [1, 9], lambda x, y: 0 < x - y < 10),
            3: ([1, 9], [1, 9], lambda x, y: x - y > 0),
            5: ([1, 9], [1.1, 9.9, 0.1], lambda x, y: x - y > 0),
            7: ([1, 9], [1.01, 9.99, 0.01]),
        },
        level,
    )
    powers_constraints = {
        1: [1, 3],
        3: [-3, 3],
        5: [-5, 5],
        7: [-5, 7],
    }
    power_1 = pick(powers_constraints, level)
    power_2 = pick(powers_constraints, level)
    return ("Work out and leave in standard form",) + stfsub(
        x * 10 ** power_1, y * 10 ** power_2
    )


def generate_stf2dec(level):
    """Standard form to ordinary"""
    return ("Convert to an ordinary number",) + generate_stf(level)[2:0:-1]


def generate_multfrac(level):
    """Multiply Fractions"""
    (a, b) = pick(
        {
            1: ([1, 1], [2, 5]),
            3: ([1, 1], [2, 9]),
            4: ([2, 9], [2, 9], condition_frac(True)),
            7: ([2, 13], [2, 13], condition_frac()),
        },
        level,
    )
    (c, d) = pick(
        {
            1: ([1, 1], [2, 5]),
            2: ([2, 2], [2, 5], condition_frac()),
            3: ([2, 5], [2, 5], condition_frac()),
            4: ([2, 9], [2, 9], condition_frac(True)),
            7: ([2, 13], [2, 13], condition_frac()),
        },
        level,
    )
    return ("Calculate the following",) + mult(nsimplify(a / b), nsimplify(c / d))


def generate_divfrac(level):
    """Divide Fractions"""
    (a, b) = pick(
        {
            1: ([1, 1], [2, 5]),
            3: ([1, 1], [2, 9]),
            4: ([2, 9], [2, 9], condition_frac(True)),
            7: ([2, 13], [2, 13], condition_frac()),
        },
        level,
    )
    (c, d) = pick(
        {
            1: ([1, 1], [2, 9]),
            3: ([2, 5], [2, 9], condition_frac()),
            4: ([2, 9], [2, 9], condition_frac(True)),
            7: ([2, 13], [2, 13], condition_frac()),
        },
        level,
    )
    return ("Calculate the following",) + div(nsimplify(a / b), nsimplify(c / d))
