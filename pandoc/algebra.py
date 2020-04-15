import re
import sympy as s
from math import log, floor

# Redefine some functions to automatically sympify
_s = lambda x: s.sympify(x, evaluate=False) if isinstance(x, (str, int)) else x
_simplify = lambda x: s.simplify(_s(x))
_expand = lambda x: s.expand(_simplify(x))
factor = lambda x: s.factor(_s(x))
def latex(expr):
    ltx = s.latex(_s(expr)).replace('cdot', 'times')
    ltx = re.sub(r'\\left\((\-[0-9]+)\\right\) ', r'\1 ', ltx)
    return ltx

def exercise(expr, callback_ex, callback_sol, **options):
    substitutions = [(s.symbols(t), s.UnevaluatedExpr(v)) for (t, v) in options.items() if t not in ['l']]
    exercise = options['l'] if 'l' in options.keys() else callback_ex(expr).subs(substitutions)
    solution = callback_sol(expr).subs(substitutions)
    return (latex(exercise), latex(solution))

simplify = lambda expr, **options: exercise(expr, _s, _simplify, **options)
expand = lambda expr, **options: exercise(expr, _s, _expand, **options)
factorise = lambda expr, **options: exercise(expr, _s, factor, **options)

def expindex(base, power):
    return (f"{{{base}}}^{{{power}}}", " \\times ".join([str(base)] * power))

def _mult(join_ex, join_sol, terms, options, cbk = latex, div = False):
    substitutions = [(s.symbols(t), s.UnevaluatedExpr(v)) for (t, v) in options.items() if t not in ['l']]
    if 'l' in options.keys():
        exercise = options['l']
    else:
        l_terms = [cbk(_s(str(t)).subs(substitutions)) for t in terms]
        # Bracket terms if necessary
        if div == True and ' ' in l_terms[1]:
            l_terms[1] = f'\\br{{{l_terms[1]}}}'
        exercise = join_ex.join(l_terms)
        if join_ex == '}{':
            exercise = f'\\frac{{{exercise}}}'
    solution = _simplify(f'({join_sol.join([str(t) for t in terms])})').subs(substitutions)
    return (exercise, cbk(solution))

mult = lambda *terms, **options: _mult('\\times ', ')*(', terms, options)
div = lambda *terms, **options: _mult('\\div ', ')/(', terms, options, latex, True)
frac = lambda *terms, **options: _mult('}{', ')/(', terms, options)
lcm = lambda *terms: (','.join([str(t) for t in terms]), s.lcm(terms))

def power(expr, power, **substitutions):
    substitutions = [(s.symbols(t), s.UnevaluatedExpr(v)) for (t, v) in substitutions.items()]
    exercise = f'\\br{{{latex(_s(expr).subs(substitutions))}}}^{{{power}}}'
    expr = f'({expr})^({power})'
    solution = latex(s.powdenest(expr, force=True).subs(substitutions))
    return (exercise, solution)

def equation(lhs, rhs = '0'):
    if isinstance(lhs, str) and '=' in lhs:
        lhs, rhs = lhs.split('=')
    lhs, rhs = _s(lhs), _s(rhs)
    exercise = f'{latex(lhs)} = {latex(rhs)}'
    solution = ', '.join([latex(sol) for sol in s.solve(lhs-rhs)])
    return (exercise, solution)

def complete_square(expr):
    alpha, h, k, x = s.symbols('alpha h k x')
    solution = alpha*(x + h)**2 + k
    sols = [y for y in s.solve(solution - _s(expr), [alpha, h, k])[0]]
    exercise = latex(expr)
    solution = latex(solution.subs(dict(zip([alpha, h, k], sols))))
    return (exercise, solution)

def showfrac(num, den, op = False, num2 = 1, den2 = 1):
    lines = ['\\begin{tikzpicture}']
    lines.append('\\draw[thick] (0, 0) circle (1cm);')
    node = f'\\frac {{{num}}}{{{den}}}'
    common_den = s.lcm(den, den2)
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

def stf(number):
    exercise = str(number)
    number = s.sympify(number)
    sign = ''
    if number < 0:
        sign = '-'
        number = -1*number
    power = floor(s.log(number) / s.log(10))
    x = number / 10**power
    x = re.sub(r'([1-9])\.?0*$', r'\1', str(x.evalf()))
    solution = f"{sign}{x} \\times 10^{{{power}}}"
    return (exercise, solution)

stf2dec = lambda x: (stf(x)[1], stf(x)[0])
_stf = lambda t: stf(t)[1]
stfmult = lambda *terms, **options: _mult(' \\times ', ')*(', terms, options, _stf)
stfdiv = lambda *terms, **options: _mult(' \\div ', ')/(', terms, options, _stf, True)
stffrac = lambda *terms, **options: _mult('}{', ')/(', terms, options, _stf)
stfadd = lambda *terms, **options: _mult(' + ', ')+(', terms, options, _stf)
stfsub = lambda *terms, **options: _mult(' - ', ')-(', terms, options, _stf)
