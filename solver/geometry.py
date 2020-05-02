from sympy import cos, latex, oo, pi, solveset, sympify
from sympy import Interval, Symbol

PI = pi
DEG = PI / 180
RAD = 180 / PI


def cosine_law(a, b, c, gamma, radians=False):
    """Apply the Law of Cosines to find an angle or a length

    Parameters
    ----------
    a : int, float, str
        First side
    b : int, float, str
        Second side
    c : int, float, str
        Third side
    gamma: int, float, str
        Angle between the first two sides in radians
    radians: bool
        Whether to use radians for the output

    Examples
    --------
    >>> cosine_law(3, 4, "c", 90*DEG)
    (..., "c = 5")
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


def pythagoras(a, b, c, radians=False):
    """Checks if right triangle, and compute required lengths

    :param a: first side
    :param b: second side
    :param c: third side
    :param radians: use radians if True, degrees otherwise
    """
    is_symbol = [isinstance(sympify(l), Symbol) for l in [a, b, c]]
    solve_for_angle = is_symbol == 3 * [False]

    if solve_for_angle:
        (data, solution) = cosine_law(a, b, c, "gamma")
        if data["sol"] == "90":
            solution = "Right triangle"
        else:
            solution = "Not a right triangle"
    else:
        (data, solution) = cosine_law(a, b, c, 90 * DEG, radians=radians)
        del data["gamma"]

    return (data, solution)
