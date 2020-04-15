import sympy as s
import re

domain = '-9:9'

def sympy2tikz(function):
    function = function.replace('x', '(\\x)')
    function = function.replace('**', '^')
    op = [m.end() for m in re.finditer('sin|cos|tan', function)]
    changes = [(pos, '(') for pos in op]
    level, levels = 0, []
    for p, c in enumerate(list(function)):
        if c == '(':
            level += 1
            if p in op:
                levels.append(level)
                pass
        elif c == ')':
            if len(levels) and level == levels[-1]:
                changes.append((p, ')r'))
                levels.pop()
            level -= 1
    for pos, str in sorted(changes, key=lambda x: x[0], reverse=True):
        function = function[:pos] + str + function[pos:]
    return function

def gradient(x1, y1, x2, y2):
    exercise = f"({x1}, {y1}), ({x2}, {y2})"
    solution = s.latex(s.sympify(f"({y2} - {y1}) / ({x2} - {x1})"))
    return (exercise, solution)

def line_equation(*args):
    exercise = f'\\text{{grad}} = {args[0]}, ({args[1]}, {args[2]})'
    args = list(args)
    if len(args) == 4:
        x1, y1, x2, y2 = args
        exercise = f'({x1}, {y1}), ({x2}, {y2})'
        args = [f"({y2} - {y1}) / ({x2} - {x1})", x2, y2]
    grad = s.sympify(args.pop(0))
    x, a, b = s.symbols('x'), s.sympify(args[0]), s.sympify(args[1])
    solution = s.latex(grad * (x - a) + b)
    return (exercise, f"y = {solution}")

def plot(function, color='darkblue', dom=False):
    global domain
    if not isinstance(function, str):
        function = str(function)
    return f'\\plotfunction[{color}]{{{dom if dom else domain}}}{{{sympy2tikz(function)}}}'

def showsecant(function, a, b, color='darkred', dom=False):
    x, expr = s.symbols('x'), s.sympify(function)
    gradient = (expr.subs(x, b) - expr.subs(x, a)) / (b - a)
    tangent = gradient*(x - a) + expr.subs(x, a)
    return plot(str(tangent), color, dom)

def showtangent(function, a, color='darkgreen', dom=False):
    x, expr = s.symbols('x'), s.sympify(function)
    gradient = s.Derivative(expr, x).doit().subs(x, a)
    tangent = gradient*(x - a) + expr.subs(x, a)
    return plot(str(tangent), color, dom)

def taylor(function, a, order):
    poly, f, x = 0, s.sympify(function), s.symbols('x')
    for i in range(0, order + 1):
        poly += (f.diff(x, i).subs(x, a))/(s.factorial(i)) * (x - a)**i
    return poly

taylor_poly = lambda f, a, n: s.latex(taylor(f, a, n))

def showtaylor(function, a, order, color='darkgreen', dom=False):
    x, expr = s.symbols('x'), s.sympify(function)
    return plot(str(taylor(function, a, order)), color, dom)

def showcoordinates(function, a, x_text, y_text):
    y = s.sympify(function).subs(s.symbols('x'), a)
    return f"""
    \draw[dashed] ({a}, 0) node[below] {{\\footnotesize ${x_text}$}} -- ({a}, {y}) -- (0, {y}) node[{'left' if a > 0 else 'right'}] {{\\footnotesize ${y_text}$}};
    \draw[fill=black] ({a}, {y}) circle (0.1);
    """.replace('\n', '')

def tikz_plot(contents, opt, fmt):
    options = {'size': 0.5, 'b': -6, 'l': -9, 'r': 9, 't': 6}
    options.update(opt)
    global domain
    domain = f"{options['l']}:{options['r']}"

    lines = [
        '\\onslide<+->{' if fmt == 'beamer' else '{',
        f"\\begin{{plot}}{{{options['size']}}}{{{options['l']}}}{{{options['b']}}}{{{options['r']}}}{{{options['t']}}}"
    ]
    for l in contents.split('\n'):
        if re.match('^[a-zA-z_,\s]*=', l):
            exec(l)
        else:
            line = eval(l)
            if fmt == 'beamer':
                line = f'\\onslide<+->{{{line}}}'
            lines.append(line)
    lines.append('\\end{plot}}')
    return '\n'.join(lines)

def integrate(expr, a = False, b = False):
    if a or b:
        expr = s.Integral(sympify(expr), (symbols('x'), a, b))
    else:
        expr = s.Integral(sympify(expr))
    exercise = s.latex(expr)
    solution = s.latex(expr.doit())
    return (exercise, solution)

def diff(*args, **options):
    args = [s.sympify(a) if isinstance(a, str) else a for a in args]
    if len(args) == 1 or isinstance(args[1], int):
        args.insert(1, s.symbols('x'))
    exercise = s.Derivative(*args)
    solution = s.expand_trig(s.simplify(exercise.doit()))
    exercise = s.latex(s.Derivative(*args))
    exercise = exercise.replace('\\partial', 'd') if not options.get('partial') else exercise
    return (exercise, s.latex(solution))

def tangent(expr, a):
    x, expr = s.symbols('x'), s.sympify(expr)
    exercise = f"y = {latex(expr)} \\text{{ at }} x = {a}"
    gradient = s.Derivative(expr, x).doit().subs(x, a)
    solution = gradient*(x - a) + expr.subs(x, a)
    solution = f"y = {latex(solution)}"
    return(exercise, solution)
