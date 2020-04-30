from solver.exercise import Exercise, latex, OpExercise, Stf, StfExercise
from sympy import (
    Add,
    expand as Expand,
    factor,
    Mul,
    Pow,
    powdenest,
    simplify as Simplify,
    solve,
    sqrt,
    symbols,
    sympify,
    UnevaluatedExpr,
)


def expand(expression):
    """Expand an algebraic expression

    Parameters
    ----------
    expression : str
        Mathematical expression to be expanded

    Examples
    --------
    >>> expand('(x - 2) * (x - 3)')
    ('(x - 2) (x - 3)', 'x^{2} - 5 x + 6')
    """
    return Exercise(latex, Expand)(expression)


def factorise(expression):
    """Factorise an algebraic expression

    Parameters
    ----------
    expression : str
        Mathematical expression to be factorised

    Examples
    --------
    >>> factorise('x^2 - 5 * x + 6')
    ('x^{2} - 5 x + 6', '(x - 2) (x - 3)')
    """
    return Exercise(latex, factor)(expression)


def simplify(expression):
    r"""Simplify an algebraic expression

    Parameters
    ----------
    expression : str
        Mathematical expression to be simplified

    Examples
    --------
    >>> symplify('x^2/x')
    ('\\frac{x^2}{x}', 'x')
    """
    return Exercise(latex, Simplify)(expression)


def Div(a, b, **kwargs):
    return Mul(a, Pow(b, -1), **kwargs)


def Subtract(a, b, **kwargs):
    return Add(a, Mul(-1, b), **kwargs)


add = OpExercise(Add)
div = OpExercise("div")
frac = OpExercise("frac")
mult = OpExercise(Mul)
subtract = OpExercise(Subtract)


def _display_float(number):
    return f"{number.evalf():.15f}".rstrip("0").rstrip(".")


stf = Exercise(_display_float, Stf)
stf2dec = Exercise(lambda t: latex(Stf(t)), _display_float)
stfadd = StfExercise(Add)
stfdiv = StfExercise("div")
stffrac = StfExercise("frac")
stfmult = StfExercise(Mul)
stfsub = StfExercise(Subtract)

expindex = Exercise(
    lambda base, power: f"{{{base}}}^{{{power}}}",
    lambda base, power: r" \times ".join([str(base)] * power),
)


def power(expr, power, **substitutions):
    substitutions = [
        (symbols(t), UnevaluatedExpr(v)) for (t, v) in substitutions.items()
    ]
    exercise = f"\\br{{{latex(sympify(expr).subs(substitutions))}}}^{{{power}}}"
    expr = f"({expr})^({power})"
    solution = latex(powdenest(expr, force=True).subs(substitutions))
    return (exercise, solution)


def equation(lhs, rhs="0"):
    if isinstance(lhs, str) and "=" in lhs:
        lhs, rhs = lhs.split("=")
    lhs, rhs = sympify(lhs), sympify(rhs)
    exercise = f"{latex(lhs)} = {latex(rhs)}"
    solution = ", ".join([latex(sol) for sol in solve(lhs - rhs)])
    return (exercise, solution)


def complete_square(expr):
    alpha, h, k, x = symbols("alpha h k x")
    solution = alpha * (x + h) ** 2 + k
    sols = [y for y in solve(solution - sympify(expr), [alpha, h, k])[0]]
    exercise = latex(expr)
    solution = latex(solution.subs(dict(zip([alpha, h, k], sols))))
    return (exercise, solution)


def circle_equation(info, lhs, rhs=0):
    if isinstance(lhs, str) and "=" in lhs:
        lhs, rhs = lhs.split("=")
    lhs, rhs = sympify(lhs), sympify(rhs)
    eq = Expand(lhs - rhs)
    exercise = f"{latex(lhs)} = {latex(rhs)}"

    # alpha [ (x - v)^2 + (y - w)^2 - r^2 ] = 0
    x, y = symbols("x y")
    alpha = eq.coeff(x, 2)
    v = -eq.coeff(x, 1) / (2 * alpha)
    w = -eq.coeff(y, 1) / (2 * alpha)
    r = sqrt(v ** 2 + w ** 2 - eq.subs([(x, 0), (y, 0)]) / alpha)

    if info == "radius":
        solution = latex(r)
    else:
        solution = f"\\br{{{latex(v)}, {latex(w)}}}"
    return (exercise, solution)
