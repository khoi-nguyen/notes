from pandocfilters import toJSONFilter, attributes, Math, Span, RawInline, RawBlock, Str
from sympy import *

# Redefine some functions to automatically sympify
s = lambda x: sympify(x) if isinstance(x, (str, int)) else x
expand2, factor2, latex2 = expand, factor, latex
del expand, factor, latex
latex = lambda x: latex2(s(x))
expand = lambda x: expand2(s(x))
factor = lambda x: factor2(s(x))

# Shortcuts
blatex = lambda x: RawBlock('latex', x)
ilatex = lambda x: RawInline('latex', x)
imath = lambda x: Math({'t': 'InlineMath'}, x)
answer = lambda x: Span(attributes({'class': 'answer'}), [imath(x)])
display = lambda ex, sol: [imath(ex), answer(sol)]

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

def plot(function, color='darkblue'):
    function = function.replace('x', '(\\x)')
    return '\\plotfunction[' + color + ']{-9:9}{' + function + '}'

def tikz_plot(contents):
    instructions = contents.split('\n')
    lines = []
    lines.append('\\begin{plot}{0.5}{-9}{-6}{9}{6}')
    for l in instructions:
        lines.append(eval(l))
    lines.append('\\end{plot}')
    return '\n'.join(lines)

def main(key, value, fmt, meta):
    if key == 'Code':
        [[ident, classes, keyvals], contents] = value
        return eval(contents)
    if key == 'CodeBlock' and fmt == 'beamer':
        [[ident, classes, keyvals], contents] = value
        return blatex(tikz_plot(contents))

if __name__ == '__main__':
    toJSONFilter(main)
