from sympy import cos, latex, oo, pi, solveset, sympify
from sympy import Interval, Symbol

PI = pi
DEG = PI / 180
RAD = 180 / PI


def cosine_law(a, b, c, gamma, radians=False):
    """Apply the Law of Cosines to find an angle or a length

    :param a: first side
    :param b: second side
    :param c: third side
    :param gamma: angle contained between the first two sides
    :param radians: use radians if True, degrees otherwise
    """
    lengths = [sympify(l) for l in [a, b, c]]
    [a, b, c] = lengths
    is_symbol = [isinstance(l, Symbol) for l in lengths]

    # Determine symbol, the sought quantity
    solve_for_angle = is_symbol == 3 * [False]
    if solve_for_angle:
        gamma = Symbol(gamma)
        symbol = gamma
    else:
        symbol = lengths[is_symbol.index(True)]

    dom = Interval(*(0, PI / 2 if solve_for_angle else oo))
    sols = solveset(
        a ** 2 + b ** 2 - 2 * a * b * cos(gamma) - c ** 2, symbol, domain=dom
    )
    sol = sols.args[0] * (1 if radians or not solve_for_angle else RAD)

    return (
        {
            "a": latex(a),
            "b": latex(b),
            "c": latex(c),
            "gamma": latex(gamma),
            "sol": latex(sol),
            "symbol": latex(symbol),
        },
        f"{latex(symbol)} = {latex(sol)}",
    )
