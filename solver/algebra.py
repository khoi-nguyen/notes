from solver.exercise import Exercise, latex, OpExercise, Stf, StfExercise
from sympy import (
    Add,
    expand as Expand,
    factor,
    Mul,
    Pow,
    powdenest,
    powsimp,
    simplify as Simplify,
    solve,
    sqrt,
    Symbol,
    symbols,
    sympify,
    UnevaluatedExpr,
)


def _exercise(solve=False, op=False, std_form=False, transform=False):
    """Template to create simple solvers

    :param solve: Sympy method to solve the exercise
    :param op: Operation
    """

    # Add, subtract, multiply, divide
    if op:
        join_str = {
            "frac": "}{",
            "div": " \\div ",
        }

        # Specify which simplifications we allow
        # e.g. allow multiplications but don't touch power bases
        def pre(term, level=0):
            args = [pre(a, level + 1) for a in term.args]
            if term.func == Mul:
                term = Mul(*args, evaluate=True)
            if term.func == Pow and not level:
                [base, power] = args
                # Ensure this is not a fraction with numerator 1
                if base.func != Symbol and power != -1:
                    term = Pow(UnevaluatedExpr(args[0]), args[1])
            return term

        def transform_term(term):
            term = pre(term)
            term = Stf(term) if std_form else term
            return latex(term)

        def transform(terms):
            if op in join_str.keys():
                terms = [transform_term(t) for t in terms]
                if op == "div" and " " in terms[1]:
                    terms[1] = f"\\br{{{terms[1]}}}"
                exercise = join_str[op].join(terms)
                if op == "frac":
                    exercise = f"\\frac{{{exercise}}}"
            else:
                terms = [Stf(t) for t in terms] if std_form else terms
                exercise = latex(
                    op(*terms, evaluate=False), mul_symbol="times", order="none"
                )
            return exercise

        def _solve(terms):
            terms = [pre(t) for t in terms]
            if op in join_str:
                return powsimp(Mul(terms[0], Pow(terms[1], -1)))
            else:
                return powsimp(op(*terms))

    else:
        if not transform:

            def transform(terms):
                return latex(terms[0])

        def _solve(terms):
            return solve(terms[0])

    def exercise(*terms):
        terms = [sympify(t, evaluate=False) for t in terms]
        exercise = transform(terms)
        solution = _solve(terms)
        solution = Stf(solution) if std_form else solution
        return (exercise, latex(solution))

    return exercise


expand = Exercise(latex, Expand)
factorise = Exercise(latex, factor)
simplify = Exercise(latex, Simplify)


def Div(a, b, **kwargs):
    return Mul(a, Pow(b, -1), **kwargs)


def Subtract(a, b, **kwargs):
    return Add(a, Mul(-1, b), **kwargs)


add = OpExercise(Add)
div = _exercise(op="div")
frac = _exercise(op="frac")
mult = OpExercise(Mul)
subtract = OpExercise(Subtract)

stfadd = StfExercise(Add)
stfdiv = _exercise(op="div", std_form=True)
stffrac = _exercise(op="frac", std_form=True)
stfmult = StfExercise(Mul)
stfsub = StfExercise(Subtract)


def expindex(base, power):
    return (f"{{{base}}}^{{{power}}}", " \\times ".join([str(base)] * power))


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


def display_float(number):
    return f"{number.evalf():.15f}".rstrip("0").rstrip(".")


stf = Exercise(display_float, Stf)


def stf2dec(number):
    return stf(number)[::-1]


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
