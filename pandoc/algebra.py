from sympy import *

# Redefine some functions to automatically sympify
s = lambda x: sympify(x, evaluate=False) if isinstance(x, (str, int)) else x
expand2, factor2, simplify2, latex2 = expand, factor, simplify, latex
del expand, factor, latex
latex = lambda x: latex2(s(x))
_expand = lambda x: expand2(s(x))
_simplify = lambda x: simplify2(s(x))
factor = lambda x: factor2(s(x))
display = lambda ex, sol: '${} \answer{{{}}}$'.format(ex, sol)

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
    return display(exercise, solution)

def div(dividend, divisor, **substitutions):
    exercise = False
    if  'l' in substitutions.keys():
        exercise = substitutions['l']
        del substitutions['l']
    substitutions = [(symbols(t), UnevaluatedExpr(v)) for (t, v) in substitutions.items()]
    tr = lambda t: latex(s(t).subs(substitutions))
    if not exercise:
        exercise = '{} \\div {}'.format(tr(dividend), tr(divisor))
    solution = _simplify('({})/({})'.format(dividend, divisor))
    solution = latex(solution.subs(substitutions)).replace('cdot', 'times')
    return display(exercise, solution)

def frac(dividend, divisor, **substitutions):
    exercise = False
    if  'l' in substitutions.keys():
        exercise = substitutions['l']
        del substitutions['l']
    substitutions = [(symbols(t), UnevaluatedExpr(v)) for (t, v) in substitutions.items()]
    tr = lambda t: latex(s(t).subs(substitutions))
    if not exercise:
        exercise = '\\frac {{{}}} {{{}}}'.format(tr(dividend), tr(divisor))
    solution = _simplify('({})/({})'.format(dividend, divisor))
    solution = latex(solution.subs(substitutions)).replace('cdot', 'times')
    return display(exercise, solution)

def power(expr, power, **substitutions):
    substitutions = [(symbols(t), UnevaluatedExpr(v)) for (t, v) in substitutions.items()]
    exercise = '\\br{{{}}}^{{{}}}'.format(latex(s(expr).subs(substitutions)), power)
    expr = '({})^({})'.format(expr, power)
    solution = latex(powdenest(expr, force=True).subs(substitutions))
    return display(exercise, solution)

def simplify(expr, l=False):
    exercise = l if l else latex(expr)
    solution = latex(_simplify(expr))
    return display(exercise, solution)

def expand(expr):
    exercise = latex(expr)
    solution = latex(_expand(_simplify(expr)))
    return display(exercise, solution)

def factorise(expr):
    exercise = latex(_expand(expr))
    solution = latex(factor(expr))
    return display(exercise, solution)

def equation(lhs, rhs = '0'):
    if isinstance(lhs, str) and '=' in lhs:
        lhs, rhs = lhs.split('=')
    lhs, rhs = s(lhs), s(rhs)
    exercise = latex(lhs) + '=' + latex(rhs)
    solution = ', '.join([latex(sol) for sol in solve(lhs-rhs)])
    return display(exercise, solution)

def complete_square(expr):
    alpha, h, k, x = symbols('alpha h k x')
    solution = alpha*(x + h)**2 + k
    sols = [y for y in solve(solution - s(expr), [alpha, h, k])[0]]
    exercise = latex(expr)
    solution = latex(solution.subs(dict(zip([alpha, h, k], sols))))
    return display(exercise, solution)

def showfrac(num, den):
    block = ['\\begin{tikzpicture}\n\\node at (0, 1.5) {']
    block.append('$\\frac {' + str(num) + '}{' + str(den) + '}$')
    block.append('};')
    lines = []
    for i in range(0, den):
        angle = 90+i*360/den
        color = 'fraction' if i < num else 'white'
        lines.append('\\draw[fill={3},thick] (0, 0) -- ({1}:{0}) arc ({1}:{2}:{0}) -- cycle;'.format('1cm', angle, angle + 360/den, color))
    lines.append('\\end{tikzpicture}')
    block.append('\n'.join(lines))
    return '\n'.join(block)
