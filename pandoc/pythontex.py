from pandocfilters import toJSONFilter, attributes, Math, Span, RawInline, RawBlock, Str
from sympy import *
from algebra import *

# Shortcuts
blatex = lambda x: RawBlock('latex', x)
ilatex = lambda x: RawInline('latex', x)
imath = lambda x: Math({'t': 'InlineMath'}, x)

domain = '-9:9'

def plot(function, color='darkblue'):
    global domain
    function = function.replace('x', '(\\x)')
    return f'\\plotfunction[{color}]{{{domain}}}{{{function}}}'

def tikz_plot(contents, opt):
    options = {'size': 0.5, 'b': -6, 'l': -9, 'r': 9, 't': 6}
    options.update(opt)
    global domain
    domain = f"{options['l']}:{options['r']}"

    lines = [f"\\begin{{plot}}{{{options['size']}}}{{{options['l']}}}{{{options['b']}}}{{{options['r']}}}{{{options['t']}}}"]
    for l in contents.split('\n'):
        lines.append(eval(l))
    lines.append('\\end{plot}')
    return '\n'.join(lines)

def main(key, value, fmt, meta):
    if key == 'Code':
        [[ident, classes, keyvals], contents] = value
        result = eval(contents)
        if isinstance(result, (str, int)):
            return [ilatex(str(result))]
        elif isinstance(result, tuple):
            return [
                imath(result[0]),
                Span(attributes({'class': 'answer'}), [imath(result[1])])
            ]
    if key == 'CodeBlock':
        [[ident, classes, keyvals], contents] = value
        if 'graph' in classes and fmt == 'beamer':
            return blatex(tikz_plot(contents, dict(keyvals)))

if __name__ == '__main__':
    toJSONFilter(main)
