from pandocfilters import toJSONFilter, attributes, Math, Span, RawInline, RawBlock, Str
from sympy import *
from algebra import *

# Shortcuts
blatex = lambda x: RawBlock('latex', x)
imath = lambda x: Math({'t': 'InlineMath'}, x)
answer = lambda x: Span(attributes({'class': 'answer'}), [imath(x)])
display = lambda ex, sol: [imath(ex), answer(sol)]

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
