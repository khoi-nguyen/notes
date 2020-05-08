from solver.helpers import display_float, pre, Round, Stf, Subtract
from solver.exercise import Exercise, EqExercise, latex, OpExercise, StfExercise
from sympy import (
    Add,
    expand as Expand,
    factor,
    Mul,
    posify,
    powdenest,
    radsimp,
    Pow,
    Rational,
    simplify as Simplify,
    solve,
    sqrt,
    Symbol,
    symbols,
    UnevaluatedExpr,
)
from sympy.parsing.latex import parse_latex


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
    return Exercise(solve=Expand)(expression)


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
    return Exercise(solve=factor)(expression)


def simplify_surds(expression):
    r"""Simplify surds an algebraic expression

    All symbols are assumed to be positive.

    Parameters
    ----------
    expression : str
        Mathematical expression to be simplified

    Examples
    --------
    >>> simplify_surds('sqrt(x^2)')
    ('\\sqrt{x^{2}}', 'x')
    """

    def surdify(expression):
        """Transform x^(p/2) to sqrt(x^p)"""
        args = [surdify(a) for a in expression.args]
        if expression.func == Pow:
            [base, power] = args
            if power.func == Rational and power.q == 2 and power.p not in [-1, 1]:
                expression = sqrt(UnevaluatedExpr(Pow(base, power.p)))
        elif expression.func in [Pow, Add, Mul]:
            expression = expression.func(*args, evaluate=False)
        return expression

    def group(expression):
        """Transform sqrt(x)*sqrt(y) to sqrt(x*y)"""
        args = [group(a) for a in expression.args]
        if expression.func == Mul:
            surds = [t for t in expression.args if t.func == Pow and t.args[1] == 1 / 2]
            if surds:
                grouped = sqrt(Mul(*[t.args[0] for t in surds]), evaluate=False)
                expression = Mul(
                    grouped,
                    *[a for a in expression.args if a not in surds],
                    evaluate=False,
                )
        elif expression.func in [Pow, Add, Mul]:
            expression = expression.func(*args, evaluate=False)
        return expression

    def solution(expression):
        expr = posify(expression)[0].doit()
        return group(surdify(radsimp(expr)))

    return Exercise(solve=solution)(expression)


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
    return Exercise(solve=Simplify)(expression)


def leval(expr, solve=Simplify):
    r"""Transform a latex expression in Sympy, then calculates it
    """
    solution = latex(solve(parse_latex(expr).doit()))
    return (expr, solution)


def add(*terms):
    r"""Add terms

    Parameters
    ----------
    terms : list
        List of strings which correspond to the mathematical expressions to add.

    Examples
    --------
    >>> add('3/4', '1/2')
    ('\\frac{3}{4} + \\frac{1}{2}', '\\frac{5}{4}')
    """
    return OpExercise(Add)(*terms)


def div(dividend, divisor):
    r"""Divide terms (with \div)

    Parameters
    ----------
    dividend : string
        Mathematical expression to divide.
    divisor : string
        What the dividend will be divided by.

    Examples
    --------
    >>> div('3/4', '2/3')
    ('\\frac{3}{4} \\div \\frac{2}{3}', '\\frac{9}{8}')
    """
    return OpExercise("div")(dividend, divisor)


def frac(numerator, denominator):
    r"""Divide terms (in fraction form)

    Parameters
    ----------
    numerator : string
        Mathematical expression to divide (numerator).
    denominator : string
        What the dividend will be divided by (denominator).

    Examples
    --------
    >>> frac('3/4', '2/3')
    ('\\frac{\\frac{3}{4}}{\\frac{2}{3}}', '\\frac{9}{8}')
    """
    return OpExercise("frac")(numerator, denominator)


def mult(*terms):
    r"""Multiply terms

    Parameters
    ----------
    terms : list
        List of strings which correspond to the mathematical expressions to multiply.

    Examples
    --------
    >>> mult('3/4', '1/2')
    ('\\frac{3}{4} \\times \\frac{1}{2}', '\\frac{3}{8}')
    """
    return OpExercise(Mul)(*terms)


def subtract(term1, term2):
    r"""Add terms

    Parameters
    ----------
    term1 : string
        Mathematical expression from which we want to subtract
    term2 : string
        Mathematical expression to subtract from 'term1'

    Examples
    --------
    >>> add('3/4', '1/2')
    ('\\frac{3}{4} + \\frac{1}{2}', '\\frac{5}{4}')
    """
    return OpExercise(Subtract)(term1, term2)


def round(number, dp=2, sf=False):
    def solution(number):
        return Round(number, dp, sf)

    return Exercise(display_float, solution)(number)


def stf(number):
    return Exercise(display_float, Stf)(number)


def stf2dec(number):
    def transform(term):
        return Stf(term)

    return Exercise(transform, display_float)(number)


def stfadd(*terms):
    return StfExercise(Add)(*terms)


def stfdiv(dividend, divisor):
    return StfExercise("div")(dividend, divisor)


def stffrac(numerator, denominator):
    return StfExercise("frac")(numerator, denominator)


def stfmult(*terms):
    return StfExercise(Mul)(*terms)


def stfsub(*terms):
    return StfExercise(Subtract)(*terms)


def expindex(base, power):
    def exercise(base, power):
        return Pow(base, power, evaluate=False)

    def solution(base, power):
        return [str(base)] * power

    return Exercise(exercise, solution, join=r" \times ")(base, power)


def power(expr, power):
    def exercise(expr, power):
        return Pow(pre(expr), power, evaluate=False)

    def solution(expr, power):
        return powdenest(Pow(pre(expr), power), force=True)

    return Exercise(exercise, solution)(expr, power)


def equation(equation):
    return EqExercise()(equation)


def equations(*equations):
    return EqExercise()(*equations)


def complete_square(expr):
    r"""Complete the square

    Parameters
    ----------
    expression : str
        Algebraic expression

    Examples
    --------
    >>> complete_square("x^2 - 7*x + 2")
    ('x^{2} - 7 x + 2', '\\left(x - \\frac{7}{2}\\right)^{2} - \\frac{41}{4}')
    """

    def solution(expr):
        alpha, h, k, x = symbols("alpha h k x")
        equation = alpha * (x + h) ** 2 + k
        sols = solve(equation - expr, [alpha, h, k], dict=True)[0]
        return equation.subs(sols)

    return Exercise(solve=solution)(expr)


def circle_equation(info, expr):
    def solution(expr):
        (alpha, h, k, x, y), r = symbols("alpha h k x y"), Symbol("r", positive=True)
        equation = Expand(expr - alpha * ((x - h) ** 2 + (y - k) ** 2 - r ** 2))
        system = [equation.coeff(*t) for t in [(x, 2), (y, 2), (x, 1), (y, 1), (x, 0)]]
        values = solve(system, (alpha, r, h, k), dict=True)[0]
        return values[r] if info == "radius" else (values[h], values[k])

    return EqExercise(solution)(expr)


def change_subject(expr, subj):
    def solution(expr):
        return solve(expr, subj, dict=True)

    return EqExercise(solution)(expr)
