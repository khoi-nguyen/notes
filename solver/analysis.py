from solver.exercise import Exercise
import figures.config as config
from sympy import (
    Derivative,
    expand_trig,
    factorial,
    FourierTransform,
    Integral,
    integrate as Integrate,
    Interval,
    latex,
    minimum as Minimum,
    oo,
    solve,
    stationary_points,
    Symbol,
    symbols,
    sympify,
    simplify as Simplify,
)
import re


def sympy2tikz(function):
    function = function.replace("x", "(\\x)")
    function = function.replace("**", "^")
    op = [m.end() for m in re.finditer("sin|cos|tan", function)]
    changes = [(pos, "(") for pos in op]
    level, levels = 0, []
    for p, c in enumerate(list(function)):
        if c == "(":
            level += 1
            if p in op:
                levels.append(level)
                pass
        elif c == ")":
            if len(levels) and level == levels[-1]:
                changes.append((p, ")r"))
                levels.pop()
            level -= 1
    for pos, str in sorted(changes, key=lambda x: x[0], reverse=True):
        function = function[:pos] + str + function[pos:]
    return function


def gradient(x1, y1, x2, y2):
    exercise = f"({x1}, {y1}), ({x2}, {y2})"
    solution = latex(sympify(f"({y2} - {y1}) / ({x2} - {x1})"))
    return (exercise, solution)


def line_equation(*args):
    exercise = f"\\text{{grad}} = {args[0]}, ({args[1]}, {args[2]})"
    args = list(args)
    if len(args) == 4:
        x1, y1, x2, y2 = args
        exercise = f"({x1}, {y1}), ({x2}, {y2})"
        args = [f"({y2} - {y1}) / ({x2} - {x1})", x2, y2]
    grad = sympify(args.pop(0))
    x, a, b = symbols("x"), sympify(args[0]), sympify(args[1])
    solution = latex(grad * (x - a) + b)
    return (exercise, f"y = {solution}")


def plot(function, color="darkblue", dom=False):
    if not isinstance(function, str):
        function = str(function)
    dom = dom if dom else config.domain
    return f"\\plotfunction[{color}]{{{dom}}}{{{sympy2tikz(function)}}}"


def showsecant(function, a, b, color="darkred", dom=False):
    x, expr = symbols("x"), sympify(function)
    gradient = (expr.subs(x, b) - expr.subs(x, a)) / (b - a)
    tangent = gradient * (x - a) + expr.subs(x, a)
    return plot(str(tangent), color, dom)


def showtangent(function, a, color="darkgreen", dom=False):
    x, expr = symbols("x"), sympify(function)
    gradient = Derivative(expr, x).doit().subs(x, a)
    tangent = gradient * (x - a) + expr.subs(x, a)
    return plot(str(tangent), color, dom)


def taylor(function, a, order):
    poly, f, x = 0, sympify(function), symbols("x")
    for i in range(0, order + 1):
        poly += (f.diff(x, i).subs(x, a)) / (factorial(i)) * (x - a) ** i
    return poly


def taylor_poly(f, a, n):
    return latex(taylor(f, a, n))


def showtaylor(function, a, order, color="darkgreen", dom=False):
    return plot(str(taylor(function, a, order)), color, dom)


def showcoordinates(function, a, x_text, y_text):
    y = sympify(function).subs(symbols("x"), a)
    return f"""
    \\draw[dashed] ({a}, 0) node[below] {{\\footnotesize ${x_text}$}} -- ({a}, {y})
    -- (0, {y}) node[{'left' if a > 0 else 'right'}] {{\\footnotesize ${y_text}$}};
    \\draw[fill=black] ({a}, {y}) circle (0.1);
    """.replace(
        "\n", ""
    )


def integrate(expr, a=False, b=False):
    if a or b:
        expr = Integral(sympify(expr), (symbols("x"), a, b))
    else:
        expr = Integral(sympify(expr))
    exercise = latex(expr)
    solution = latex(expr.doit())
    return (exercise, solution)


def average(expr, a, b):
    def exercise(expr, a, b):
        expr, interval = latex(expr), latex(Interval(a, b))
        return f"{expr} on {interval}"

    def solution(expr, a, b):
        return Integrate(expr, ("x", a, b)) / (b - a)

    return Exercise(exercise, solution)(expr, a, b)


def diff(*args, **options):
    args = [sympify(a) if isinstance(a, str) else a for a in args]
    if len(args) == 1 or isinstance(args[1], int):
        args.insert(1, symbols("x"))
    exercise = Derivative(*args)
    solution = expand_trig(Simplify(exercise.doit()))
    exercise = latex(Derivative(*args))
    exercise = (
        exercise.replace("\\partial", "d") if not options.get("partial") else exercise
    )
    return (exercise, latex(solution))


def tangent(expr, a):
    x, expr = symbols("x"), sympify(expr)
    exercise = f"y = {latex(expr)} \\text{{ at }} x = {a}"
    gradient = Derivative(expr, x).doit().subs(x, a)
    solution = gradient * (x - a) + expr.subs(x, a)
    solution = f"y = {latex(solution)}"
    return (exercise, solution)


def stationary(expr):
    f = sympify(expr)
    x = symbols("x")
    st_pts = stationary_points(f, x)
    exercise = latex(f)
    solution = latex(st_pts)
    return (exercise, solution)


def minimum(expr, a=-oo, b=oo):
    f = sympify(expr)
    x = symbols("x")
    dom = Interval(a, b)
    y_min = Minimum(f, x, dom)
    x_min = solve(f - y_min, x)
    exercise = latex(f)
    solution = ", ".join([latex(i) for i in x_min])
    return (exercise, solution)


def maximum(expr, a=-oo, b=oo):
    return minimum(f"-({expr})", a, b)


def fourier(expr, xi="xi"):
    def exercise(expr, xi):
        return latex(FourierTransform(expr, Symbol("x"), xi))

    def solution(expr, xi):
        return latex(FourierTransform(expr, Symbol("x"), xi).doit())

    return Exercise(exercise, solution)(expr, xi)
