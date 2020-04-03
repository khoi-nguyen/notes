from sympy import *
from math import copysign as sign

# Redefine some functions to automatically sympify
s = lambda x: sympify(x, evaluate=False) if isinstance(x, (str, int)) else x
expand2, factor2, simplify2, latex2 = expand, factor, simplify, latex
_lcm = lcm
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

def expindex(base, power):
    return (f"{{{base}}}^{{{power}}}", " \\times ".join([str(base)] * power))

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
lcm = lambda *terms: (','.join([str(t) for t in terms]), _lcm(terms))

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

def showfrac(num, den, op = False, num2 = 1, den2 = 1):
    lines = ['\\begin{tikzpicture}']
    lines.append('\\draw[thick] (0, 0) circle (1cm);')
    node = f'\\frac {{{num}}}{{{den}}}'
    common_den = _lcm(den, den2)
    slices = [(num, den, 'fill=fraction,thick')]
    style = 'thick'
    if op:
        node += f'{op}\\frac {{{num2}}}{{{den2}}}'
        if op == '+':
            slices.append((num2, -den2, 'fill=fraction2,thick'))
        else:
            slices.append((num2, den2, 'color=darkred, pattern=north west lines, pattern color=darkred, thick'))
        if den != den2:
            style = 'gray, dotted'
    slices.append((common_den, common_den, style))
    for (n, denominator, option) in slices:
        for i in range(0, n):
            angle = 90 + i*360/denominator
            lines.append(f'\\draw[{option}] (0, 0) -- ({angle}:1cm) arc ({angle}:{angle + 360/denominator}:1cm) -- cycle;')
    lines.append(f'\\node at (0, 1.5) {{${node}$}};')
    lines.append('\\end{tikzpicture}')
    return '\n'.join(lines)

def rectfrac(num, den, num2 = 1, den2 = 1, side = 4):
    lines = ['\\begin{tikzpicture}']
    lines.append(f'\\draw (0, 0) rectangle ({side}, {side});')
    if num2 != 1 or den2 != 1:
        lines.append(f'\\draw[fill=lightblue] (0, 0) rectangle ({num/den*side}, {side});')
    lines.append(f'\\draw[thick, color=darkblue, pattern=north west lines, pattern color=darkblue] (0, 0) rectangle ({num/den*side}, {num2/den2*side});')
    for i in range(0, den):
        lines.append(f'\\draw ({i*side/den}, 0) -- ({i*side/den}, {side});')
    for i in range(0, den2):
        lines.append(f'\\draw (0, {i*side/den2}) -- ({side}, {i*side/den2});')
    lines.append('\\end{tikzpicture}')
    return '\n'.join(lines)
