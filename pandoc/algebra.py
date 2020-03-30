from sympy import *

# Redefine some functions to automatically sympify
s = lambda x: sympify(x, evaluate=False) if isinstance(x, (str, int)) else x
expand2, factor2, simplify2, latex2 = expand, factor, simplify, latex
del expand, factor, latex
latex = lambda x: latex2(s(x)).replace('cdot', 'times')
_simplify = lambda x: simplify2(s(x))
_expand = lambda x: expand2(_simplify(x))
factor = lambda x: factor2(s(x))

def exercise(expr, callback_ex, callback_sol, **options):
    substitutions = [(symbols(t), UnevaluatedExpr(v)) for (t, v) in options.items() if t not in ['l']]
    exercise = options['l'] if 'l' in options.keys() else callback_ex(expr).subs(substitutions)
    solution = callback_sol(expr).subs(substitutions)
    return (latex(exercise), latex(solution))

simplify = lambda expr, **options: exercise(expr, s, _simplify, **options)
expand = lambda expr, **options: exercise(expr, s, _expand, **options)
factorise = lambda expr, **options: exercise(expr, s, factor, **options)

def _mult(join_ex, join_sol, terms, options):
    substitutions = [(symbols(t), UnevaluatedExpr(v)) for (t, v) in options.items() if t not in ['l']]
    if 'l' in options.keys():
        exercise = options['l']
    else:
        exercise = join_ex.join([latex(s(t).subs(substitutions)) for t in terms])
        if join_ex == '}{':
            exercise = f'\\frac{{{exercise}}}'
    solution = _simplify(f'({join_sol.join([str(t) for t in terms])})').subs(substitutions)
    return (exercise, latex(solution))

mult = lambda *terms, **options: _mult('\\times ', ')*(', terms, options)
div = lambda *terms, **options: _mult('\\div ', ')/(', terms, options)
frac = lambda *terms, **options: _mult('}{', ')/(', terms, options)

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

def showfrac(num, den, latex=True):
    lines = ['\\begin{tikzpicture}']
    if latex:
        lines.append(f'\\node at (0, 1.5) {{$\\frac {{{num}}}{{{den}}}$}};')
    for i in range(0, den):
        angle = 90+i*360/den
        color = 'fraction' if i < num else 'white'
        lines.append(f'\\draw[fill={color},thick] (0, 0) -- ({angle}:1cm) arc ({angle}:{angle + 360/den}:1cm) -- cycle;')
    lines.append('\\end{tikzpicture}')
    return '\n'.join(lines)

def showsum(num, den, num2, den2):
    lines = ['\\begin{tikzpicture}']
    lines.append('\\draw[thick] (0, 0) circle (1cm);')
    if latex:
        lines.append(f'\\node at (0, 1.5) {{$\\frac {{{num}}}{{{den}}} + \\frac {{{num2}}}{{{den2}}}$}};')
    for i in range(0, num):
        angle = 90 + i*360/den
        color = 'fraction'
        lines.append(f'\\draw[fill={color},thick] (0, 0) -- ({angle}:1cm) arc ({angle}:{angle + 360/den}:1cm) -- cycle;')
    for i in range(0, num2):
        angle = 90 - i*360/den2
        color = 'fraction2'
        lines.append(f'\\draw[fill={color},thick] (0, 0) -- ({angle}:1cm) arc ({angle}:{angle - 360/den2}:1cm) -- cycle;')
    common_den = lcm(den, den2)
    for i in range(0, common_den):
        angle = 90 + i*360/common_den
        lines.append(f'\\draw[ghtgray,dotted] (0, 0) -- ({angle}:1cm) arc ({angle}:{angle}:1cm) -- cycle;')
    lines.append('\\end{tikzpicture}')
    return '\n'.join(lines)

def rectfrac(num, den, num2 = 1, den2 = 1, side = 5):
    lines = ['\\begin{tikzpicture}']
    lines.append(f'\\draw (0, 0) rectangle ({side}, {side});')
    lines.append(f'\\draw[fill=fraction] (0, 0) rectangle ({num/den*side}, {num2/den2*side});')
    for i in range(0, den):
        lines.append(f'\\draw ({i*side/den}, 0) -- ({i*side/den}, {side});')
    for i in range(0, den2):
        lines.append(f'\\draw (0, {i*side/den2}) -- ({side}, {i*side/den2});')
    lines.append('\\end{tikzpicture}')
    return '\n'.join(lines)
