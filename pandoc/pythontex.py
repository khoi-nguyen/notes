from pandocfilters import toJSONFilter, attributes, Math, Span, RawInline, RawBlock, Str
from sympy import *

# Redefine some functions to automatically sympify
s = lambda x: sympify(x, evaluate=False) if isinstance(x, (str, int)) else x
expand2, factor2, simplify2, latex2 = expand, factor, simplify, latex
del expand, factor, latex
latex = lambda x: latex2(s(x))
expand = lambda x: expand2(s(x))
simplify = lambda x: simplify2(s(x))
factor = lambda x: factor2(s(x))

# Shortcuts
blatex = lambda x: RawBlock('latex', x)
ilatex = lambda x: RawInline('latex', x)
imath = lambda x: Math({'t': 'InlineMath'}, x)
answer = lambda x: Span(attributes({'class': 'answer'}), [imath(x)])
display = lambda ex, sol: [imath(ex), answer(sol)]

def mult(*terms, **substitutions):
    substitutions = [(symbols(t), UnevaluatedExpr(v)) for (t, v) in substitutions.items()]
    exercise = [s(t).subs(substitutions) for t in terms]
    exercise = ' \\times '.join([latex(t) for t in exercise])
    solution = simplify('(' + ')*('.join([str(t) for t in terms]) + ')')
    solution = latex(solution.subs(substitutions)).replace('cdot', 'times')
    return display(exercise, solution)

def div(dividend, divisor, **substitutions):
    substitutions = [(symbols(t), UnevaluatedExpr(v)) for (t, v) in substitutions.items()]
    tr = lambda t: latex(s(t).subs(substitutions))
    exercise = '{} \\div {}'.format(tr(dividend), tr(divisor))
    solution = simplify('({})/({})'.format(dividend, divisor))
    solution = latex(solution.subs(substitutions)).replace('cdot', 'times')
    return display(exercise, solution)

def frac(dividend, divisor, **substitutions):
    substitutions = [(symbols(t), UnevaluatedExpr(v)) for (t, v) in substitutions.items()]
    tr = lambda t: latex(s(t).subs(substitutions))
    exercise = '\\frac {{{}}} {{{}}}'.format(tr(dividend), tr(divisor))
    solution = simplify('({})/({})'.format(dividend, divisor))
    solution = latex(solution.subs(substitutions)).replace('cdot', 'times')
    return display(exercise, solution)

def evaluate(expr):
    exercise = latex(expr)
    solution = latex(simplify(expr))
    return display(exercise, solution)

def expandex(expr):
    exercise = latex(expr)
    solution = latex(expand(expr))
    return display(exercise, solution)

def factorise(expr):
    exercise = latex(expand(expr))
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

domain = '-9:9'

def plot(function, color='darkblue'):
    global domain
    function = function.replace('x', '(\\x)')
    return '\\plotfunction[' + color + ']{' + domain + '}{' + function + '}'

def tikz_plot(contents, opt):
    options = {
        'size': 0.5,
        'b': -6,
        'l': -9,
        'r': 9,
        't': 6,
    }
    options.update(opt)
    global domain
    domain = '{}:{}'.format(options['l'], options['r'])

    lines = []
    lines.append('\\begin{{plot}}{{{}}}{{{}}}{{{}}}{{{}}}{{{}}}'.format(
        options['size'],
        options['l'],
        options['b'],
        options['r'],
        options['t']
    ))

    instructions = contents.split('\n')
    for l in instructions:
        lines.append(eval(l))
    lines.append('\\end{plot}')
    return '\n'.join(lines)

def showfrac(num, den):
    block = [ilatex('\\begin{tikzpicture}\n\\node at (0, 1.5) {')]
    block.append(imath('\\frac {' + str(num) + '}{' + str(den) + '}'))
    block.append(ilatex('};'))
    lines = []
    for i in range(0, den):
        angle = 90+i*360/den
        color = 'fraction' if i < num else 'white'
        lines.append('\\draw[fill={3},thick] (0, 0) -- ({1}:{0}) arc ({1}:{2}:{0}) -- cycle;'.format('1cm', angle, angle + 360/den, color))
    lines.append('\\end{tikzpicture}')
    block.append(ilatex('\n'.join(lines)))
    return block

def main(key, value, fmt, meta):
    if key == 'Code':
        [[ident, classes, keyvals], contents] = value
        result = eval(contents)
        return [imath(str(result))] if isinstance(result, (str, int)) else result
    if key == 'CodeBlock':
        [[ident, classes, keyvals], contents] = value
        if 'graph' in classes and fmt == 'beamer':
            return blatex(tikz_plot(contents, dict(keyvals)))

if __name__ == '__main__':
    toJSONFilter(main)
