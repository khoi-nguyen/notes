from sympy import *

# Redefine some functions to automatically sympify
s = lambda x: sympify(x, evaluate=False) if isinstance(x, (str, int)) else x
expand2, factor2, simplify2, latex2 = expand, factor, simplify, latex
del expand, factor, latex
latex = lambda x: latex2(s(x))
_simplify = lambda x: simplify2(s(x))
_expand = lambda x: expand2(_simplify(x))
factor = lambda x: factor2(s(x))

def exercise(expr, callback_ex, callback_sol):
    exercise = latex(callback_ex(expr))
    solution = latex(callback_sol(expr))
    return (exercise, solution)

_ = lambda x: x
simplify = lambda expr: exercise(expr, _, _simplify)
expand = lambda expr: exercise(expr, _, _expand)
factorise = lambda expr: exercise(expr, _, factor)

def mult(*terms, **substitutions):
    exercise = False
    if  'l' in substitutions.keys():
        exercise = substitutions['l']
        del substitutions['l']
    substitutions = [(symbols(t), UnevaluatedExpr(v)) for (t, v) in substitutions.items()]
    if not exercise:
        exercise = [s(t).subs(substitutions) for t in terms]
        exercise = ' \\times '.join([latex(t) for t in exercise])
    solution = _simplify('(' + ')*('.join([str(t) for t in terms]) + ')')
    solution = latex(solution.subs(substitutions)).replace('cdot', 'times')
    return (exercise, solution)

def div(dividend, divisor, **substitutions):
    exercise = False
    if  'l' in substitutions.keys():
        exercise = substitutions['l']
        del substitutions['l']
    substitutions = [(symbols(t), UnevaluatedExpr(v)) for (t, v) in substitutions.items()]
    tr = lambda t: latex(s(t).subs(substitutions))
    if not exercise:
        exercise = f'{tr(dividend)} \\div {tr(divisor)}'
    solution = _simplify(f'({dividend})/({divisor})')
    solution = latex(solution.subs(substitutions)).replace('cdot', 'times')
    return (exercise, solution)

def frac(dividend, divisor, **substitutions):
    exercise = False
    if  'l' in substitutions.keys():
        exercise = substitutions['l']
        del substitutions['l']
    substitutions = [(symbols(t), UnevaluatedExpr(v)) for (t, v) in substitutions.items()]
    tr = lambda t: latex(s(t).subs(substitutions))
    if not exercise:
        exercise = f'\\frac {{{tr(dividend)}}} {{{tr(divisor)}}}'
    solution = _simplify(f'({dividend})/({divisor})')
    solution = latex(solution.subs(substitutions)).replace('cdot', 'times')
    return (exercise, solution)

def power(expr, power, **substitutions):
    substitutions = [(symbols(t), UnevaluatedExpr(v)) for (t, v) in substitutions.items()]
    exercise = f'\\br{{{latex(s(expr).subs(substitutions))}}}^{{{power}}}'
    expr = f'({expr})^({power})'
    solution = latex(powdenest(expr, force=True).subs(substitutions))
    return (exercise, solution)

def equation(lhs, rhs = '0'):
    if isinstance(lhs, str) and '=' in lhs:
        lhs, rhs = lhs.split('=')
    lhs, rhs = s(lhs), s(rhs)
    exercise = f'{latex(lhs)} = {latex(rhs)}'
    solution = ', '.join([latex(sol) for sol in solve(lhs-rhs)])
    return (exercise, solution)

def complete_square(expr):
    alpha, h, k, x = symbols('alpha h k x')
    solution = alpha*(x + h)**2 + k
    sols = [y for y in solve(solution - s(expr), [alpha, h, k])[0]]
    exercise = latex(expr)
    solution = latex(solution.subs(dict(zip([alpha, h, k], sols))))
    return (exercise, solution)

def showfrac(num, den):
    block = [f'\\begin{{tikzpicture}}\n\\node at (0, 1.5) {{$\\frac {{{num}}}{{{den}}}$}};']
    lines = []
    for i in range(0, den):
        angle = 90+i*360/den
        color = 'fraction' if i < num else 'white'
        lines.append(f'\\draw[fill={color},thick] (0, 0) -- ({angle}:1cm) arc ({angle}:{angle + 360/den}:1cm) -- cycle;')
    lines.append('\\end{tikzpicture}')
    block.append('\n'.join(lines))
    return '\n'.join(block)
