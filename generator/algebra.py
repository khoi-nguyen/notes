from solver.algebra import (
    add,
    circle_equation,
    complete_square,
    div,
    equation,
    expindex,
    mult,
    power,
    simplify_surds,
    stf,
    stfmult,
    stfadd,
    stfdiv,
    stfsub,
    subtract,
)
from math import gcd
from generator.helpers import pick
from random import choice, randint

from sympy import (
    Abs,
    evaluate,
    expand as Expand,
    nsimplify,
    sign,
    sqrt,
    symbols,
)


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


# ---------
# Fractions
# ---------


def fraction_exercise(level, function):
    def coprime(a, b):
        return gcd(a, b) == 1

    def coprime_ordered(a, b):
        return a < b and gcd(a, b) == 1

    (a, b) = pick(
        {
            1: ([1, 1], [2, 5]),
            3: ([1, 1], [2, 9]),
            4: ([2, 9], [2, 9], coprime_ordered),
            7: ([2, 13], [2, 13], coprime),
        },
        level,
    )
    (c, d) = pick(
        {
            1: ([1, 1], [2, 5]),
            2: ([2, 2], [2, 5], coprime),
            3: ([2, 5], [2, 5], coprime),
            4: ([2, 9], [2, 9], coprime_ordered),
            7: ([2, 13], [2, 13], coprime),
        },
        level,
    )
    return ("Calculate the following",) + function(nsimplify(a / b), nsimplify(c / d))


def generate_addfrac(level):
    """Add Fractions"""
    return fraction_exercise(level, add)


def generate_subtractfrac(level):
    """Subtract Fractions"""
    return fraction_exercise(level, subtract)


def generate_divfrac(level):
    """Divide Fractions"""
    return fraction_exercise(level, div)


def generate_multfrac(level):
    """Multiply Fractions"""
    return fraction_exercise(level, mult)


def generate_equation(level):
    """Linear equation

    Parameters
    ----------
    level : int
        Difficulty level between 1 and 9

    Level
    -----
    1: 1-step, unknown on one side, positive coefficients, positive integer result
    2: 1-step, unknown on either side, positive/negative coefficients, integer result
    3: 1-step, unknown on either side, positive/negative coefficients, fractional result
    4: 2-step, unknown on either side, positive coefficients, positive integer result
    5: 2-step, unknown on either side, positive/negative coefficients, integer result
    6: 2-step, unknown on either side, positive/negative coefficients, fractional result
    7: Unknown on both sides, positive coefficients, positive integer result
    8: Unknown on both sides, positive/negative coefficients, integer result
    9: Unknown on both sides, positive/negative coefficients, fractional result
    """
    x = symbols("x")
    p_1, p_2 = choice([-1, 1]), choice([-1, 1])

    def p(x, p_y):
        return x ** p_y if x != 0 and level != 7 else x

    (a, b, c, d) = pick(
        {
            1: (
                [1, 5],
                [0, 4],
                [0, 0],
                [1, 20],
                lambda a, b, c, d: (
                    (a == 1 and b != 0 and d - b > 0)
                    or ((a - 1) * d != 0 and b == 0 and d % a)
                ),
            ),
            2: (
                [-5, 5],
                [-6, 4],
                [0, 0],
                [-9, 9],
                lambda a, b, c, d: (
                    (a == 1 and b * (b - d) != 0)
                    or ((a - 1) * a * d != 0 and b == 0 and d % p(a, p_1) == 0)
                ),
            ),
            3: (
                [-5, 5],
                [-6, 4],
                [0, 0],
                [-9, 9],
                lambda a, b, c, d: (
                    (a == 1 and b * (b - d) != 0) or (b == 0 and (a - 1) * a * d != 0)
                ),
            ),
            4: (
                [2, 5],
                [2, 5],
                [0, 0],
                [1, 20],
                lambda a, b, c, d: (d - b) % p(a, p_1) == 0 and d - b > 0,
            ),
            5: (
                [-5, 5],
                [-6, 4],
                [0, 0],
                [-9, 9],
                lambda a, b, c, d: a * (1 - a) * (b - d) != 0
                and (d - b) % p(a, p_1) == 0,
            ),
            6: (
                [-5, 5],
                [-6, 4],
                [0, 0],
                [-9, 9],
                lambda a, b, c, d: a * (1 - a) * (b - d) != 0,
            ),
            7: (
                [1, 10],
                [1, 10],
                [1, 10],
                [1, 10],
                lambda a, b, c, d: a > c
                and (d - b) % (p(a, p_1) - p(c, p_2)) == 0
                and d - b > 0,
            ),
            8: (
                [-10, 10],
                [-10, 10],
                [-10, 10],
                [-10, 10],
                lambda a, b, c, d: a * b * c * d * (b - d) * (p(a, p_1) - p(c, p_2))
                != 0,
            ),
            9: (
                [-9, 9],
                [-9, 9],
                [-9, 9],
                [-9, 9],
                lambda a, b, c, d: a * b * c * d * (b - d) * (p(a, p_1) - p(c, p_2))
                != 0,
            ),
        },
        level,
    )
    lhs = nsimplify(p(a, p_1) * x + b)
    rhs = nsimplify(p(c, p_2) * x + d)
    if level >= 2 and randint(0, 1):
        lhs, rhs = rhs, lhs
    return ("Solve",) + equation(f"{lhs} = {rhs}")


def generate_expindex(level):
    """Expanding powers"""
    base = randint(2, 9)
    power = randint(2, 5)
    return ("Expand the power",) + expindex(base, power)


def index_exercise(level, function):
    variables = ["a", "b", "c", "m", "n", "x", "y", "z"]
    base = pick({1: [2, 5], 3: variables, 7: variables + list(range(2, 10))}, level)
    powers_constraints = {
        1: [1, 3],
        3: [1, 5],
        4: [1, 9],
        5: [-9, 9],
    }
    power_1 = pick(powers_constraints, level)
    power_2 = pick(powers_constraints, level)
    return ("Simplify the following",) + function(
        f"{base}^{power_1}", f"{base}^{power_2}"
    )


def generate_multindex(level):
    """Multiply Indices"""
    return index_exercise(level, mult)


def generate_divindex(level):
    """Divide Indices"""
    return index_exercise(level, div)


def generate_powindex(level):
    """Index to power"""
    variables = list(symbols("a b c m n x y z"))
    base_1 = pick({1: [1, 3], 3: variables + list(range(2, 4))}, level)
    base_2 = pick({1: variables}, level)
    exponent = pick({1: [2, 3], 3: [2, 4], 5: [-2, 4], 7: [-4, 4]}, level)
    expr = base_1 ** (
        1 if isinstance(base_1, int) else randint(1, 3)
    ) * base_2 ** randint(1, 5)
    return ("Simplify the following",) + power(expr, exponent)


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
    return ("Solve",) + equation(str(lhs) + "=" + str(rhs))


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

    def bound_distance(C):
        return lambda p1, p2: Abs(p1 - p2) <= C

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


def generate_divsurd(level):
    """Divide Surds

    Parameters
    ----------
    level : int
        Difficulty level between 1 and 9

    Level
    -----
    1: Integer result and square number surds
    2: Fractional result and square number surds
    3: Simple surd result
    5: Fractional coefficient * surd
    7: One variable surd
    8: Two variable surd
    """
    (p1, p2, p3, p4) = pick(
        {
            1: ([2, 2], [1, 1], [2, 2], [1, 1]),
            7: ([1, 1], [0, 3], [1, 1], [0, 3], lambda p1, p2, p3, p4: p2 != p4),
            8: (
                [1, 4],
                [0, 4],
                [1, 4],
                [0, 4],
                lambda p1, p2, p3, p4: p2 != p4 and p1 != p3,
            ),
        },
        level,
    )
    variables = list(symbols("a b c m n x y z"))
    (a, b, c, d) = pick(
        {
            1: (
                [2, 12],
                [1, 1],
                [2, 12],
                [1, 1],
                lambda a, b, c, d: b == d and a != c and a % c == 0,
            ),
            2: ([2, 12], [1, 1], [2, 12], [1, 1], lambda a, b, c, d: b == d and a != c),
            3: (
                [1, 1],
                [2, 15],
                [1, 1],
                [2, 15],
                lambda a, b, c, d: b % d == 0
                and b != d
                and a ** p1 * b ** p2 != c ** p3 * d ** p4,
            ),
            5: (
                [2, 12],
                [2, 12],
                [2, 12],
                [2, 12],
                lambda a, b, c, d: b % d == 0
                and a != c
                and b != d
                and a ** p1 * b ** p2 <= 144
                and c ** p3 * d ** p4 <= 144
                and a ** p1 * b ** p2 != c ** p3 * d ** p4,
            ),
            7: (
                variables,
                variables,
                variables,
                variables,
                lambda a, b, c, d: a == b == c == d,
            ),
            8: (
                variables,
                variables,
                variables,
                variables,
                lambda a, b, c, d: a == c and b == d,
            ),
        },
        level,
    )
    with evaluate(False):
        expr = sqrt(a ** p1 * b ** p2) / sqrt(c ** p3 * d ** p4)
    return ("Simplify the following",) + simplify_surds(expr)
