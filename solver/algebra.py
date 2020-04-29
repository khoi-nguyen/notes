import re
from math import floor
from sympy import (
    expand as Expand,
    factor,
    latex as Latex,
    lcm as Lcm,
    log,
    N,
    powdenest,
    simplify as Simplify,
    solve,
    sqrt,
    symbols,
    sympify as Sympify,
    UnevaluatedExpr,
)


def sympify(expr):
    return Sympify(expr, evaluate=False)


def latex(expr):
    if isinstance(expr, str):
        expr = Sympify(expr)
    ltx = Latex(expr).replace("cdot", "times")
    ltx = re.sub(r"\\left\((\-[0-9]+)\\right\) ", r"\1 ", ltx)
    return ltx


def _algebra_exercise(solve):
    """Template to create simple solvers

    :param solve: Sympy method to solve the exercise
    """

    def exercise(expr):
        expr = Sympify(expr, evaluate=False)
        exercise = expr
        solution = solve(exercise)
        return (latex(exercise), latex(solution))

    return exercise


expand = _algebra_exercise(Expand)
factorise = _algebra_exercise(factor)
simplify = _algebra_exercise(Simplify)


def expindex(base, power):
    return (f"{{{base}}}^{{{power}}}", " \\times ".join([str(base)] * power))


def _mult(join_ex, join_sol, terms, options, cbk=latex, div=False):
    substitutions = [
        (symbols(t), UnevaluatedExpr(v)) for (t, v) in options.items() if t not in ["l"]
    ]
    if "l" in options.keys():
        exercise = options["l"]
    else:
        l_terms = [cbk(sympify(str(t)).subs(substitutions)) for t in terms]
        # Bracket terms if necessary
        if div and " " in l_terms[1]:
            l_terms[1] = f"\\br{{{l_terms[1]}}}"
        exercise = join_ex.join(l_terms)
        if join_ex == "}{":
            exercise = f"\\frac{{{exercise}}}"
    solution = Simplify(f"({join_sol.join([str(t) for t in terms])})").subs(
        substitutions
    )
    return (exercise, cbk(solution))


mult = lambda *terms, **options: _mult("\\times ", ")*(", terms, options)
div = lambda *terms, **options: _mult("\\div ", ")/(", terms, options, latex, True)
frac = lambda *terms, **options: _mult("}{", ")/(", terms, options)
lcm = lambda *terms: (",".join([str(t) for t in terms]), Lcm(terms))
add = lambda *terms, **options: _mult(" + ", ")+(", terms, options)
subtract = lambda *terms, **options: _mult(" - ", ")-(", terms, options)


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


def stf(number):
    exercise = re.sub(r"([1-9])\.?0*\s*$", r"\1", f"{N(number):.15f}")
    exercise = re.sub(r"\.0*$", "", exercise)
    number = sympify(str(number))
    sign = ""
    if number < 0:
        sign = "-"
        number = -1 * number
    power = floor(log(number) / log(10))
    x = number / 10 ** power
    x = re.sub(r"([1-9])\.?0*$", r"\1", str(x.evalf()))
    solution = f"{sign}{x} \\times 10^{{{power}}}"
    return (exercise, solution)


stf2dec = lambda x: (stf(x)[1], stf(x)[0])
_stf = lambda t: stf(t)[1]
stfmult = lambda *terms, **options: _mult(" \\times ", ")*(", terms, options, _stf)
stfdiv = lambda *terms, **options: _mult(" \\div ", ")/(", terms, options, _stf, True)
stffrac = lambda *terms, **options: _mult("}{", ")/(", terms, options, _stf)
stfadd = lambda *terms, **options: _mult(" + ", ")+(", terms, options, _stf)
stfsub = lambda *terms, **options: _mult(" - ", ")-(", terms, options, _stf)


def circle_equation(info, lhs, rhs=0):
    if isinstance(lhs, str) and "=" in lhs:
        lhs, rhs = lhs.split("=")
    eq = Expand(sympify(lhs) - sympify(rhs))
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
