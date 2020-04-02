from sympy import Integral, symbols, latex, sympify, Derivative
import re

domain = '-9:9'

def plot(function, color='darkblue'):
    global domain
    function = function.replace('x', '(\\x)')
    return f'\\plotfunction[{color}]{{{domain}}}{{{function}}}'

def showtangent(function, a, color='darkgreen'):
    global domain
    x, expr = symbols('x'), sympify(function)
    gradient = Derivative(expr, x).doit().subs(x, a)
    tangent = gradient*(x - a) + expr.subs(x, a)
    return plot(str(tangent), color)

def tikz_plot(contents, opt):
    options = {'size': 0.5, 'b': -6, 'l': -9, 'r': 9, 't': 6}
    options.update(opt)
    global domain
    domain = f"{options['l']}:{options['r']}"

    lines = [f"\\begin{{plot}}{{{options['size']}}}{{{options['l']}}}{{{options['b']}}}{{{options['r']}}}{{{options['t']}}}"]
    for l in contents.split('\n'):
        if re.match('[a-zA-z_-]*\s*=', l):
            exec(l)
        else:
            lines.append(eval(l))
    lines.append('\\end{plot}')
    return '\n'.join(lines)

def integrate(expr, a = False, b = False):
    if a or b:
        expr = Integral(sympify(expr), (symbols('x'), a, b))
    else:
        expr = Integral(sympify(expr))
    exercise = latex(expr)
    solution = latex(expr.doit())
    return (exercise, solution)

def diff(*args):
    args = [sympify(a) if isinstance(a, str) else a for a in args]
    exercise = Derivative(*args)
    solution = exercise.doit()
    return (latex(exercise), latex(solution))

def tangent(expr, a):
    x, expr = symbols('x'), sympify(expr)
    exercise = f"y = {latex(expr)} \\text{{ at }} x = {a}"
    gradient = Derivative(expr, x).doit().subs(x, a)
    solution = gradient*(x - a) + expr.subs(x, a)
    solution = f"y = {latex(solution)}"
    return(exercise, solution)
