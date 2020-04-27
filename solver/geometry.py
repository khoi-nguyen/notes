import sympy as s

PI = s.pi
DEG = PI / 180
RAD = 180 / PI


def cosine_law(a, b, c, gamma="gamma", radians=False):
    """Apply the Law of Cosines to find an angle or a length

    :param a: first side
    :param b: second side
    :param c: third side
    :param gamma: angle contained between the first two sides
    :param radians: use radians if True, degrees otherwise
    """
    lengths = [s.sympify(l) for l in [a, b, c]]
    [a, b, c] = lengths
    is_symbol = [isinstance(l, s.Symbol) for l in lengths]

    # Determine symbol, the sought quantity
    solve_for_angle = is_symbol == 3 * [False]
    if solve_for_angle:
        gamma = s.Symbol(gamma)
        symbol = gamma
    else:
        symbol = lengths[is_symbol.index(True)]

    dom = s.Interval(*(0, PI / 2 if solve_for_angle else s.oo))
    sols = s.solveset(
        a ** 2 + b ** 2 - 2 * a * b * s.cos(gamma) - c ** 2, symbol, domain=dom
    )
    sol = sols.args[0] * (1 if radians or not solve_for_angle else RAD)

    exercise = f"{a}, {b}, {c}, {gamma}"
    solution = f"{s.latex(symbol)} = {s.latex(sol)}"
    return (exercise, solution)
