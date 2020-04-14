from pandocfilters import toJSONFilter, attributes, Math, Span, RawInline, RawBlock, Str
from algebra import *
from analysis import *
from stats import *
from probability import *
from tikz import *

oo = s.oo

# Shortcuts
blatex = lambda x: RawBlock('latex', x)
ilatex = lambda x: RawInline('latex', x)
imath = lambda x: Math({'t': 'InlineMath'}, x)

answer = lambda x: ('', x[1]) if isinstance(x, tuple) else ('', x)
question = lambda x: x[0]

def main(key, value, fmt, meta):
    if key == 'Code':
        [[ident, classes, keyvals], contents] = value
        result = eval(contents)
        if isinstance(result, (str, int, float)):
            return [ilatex(str(result))]
        elif isinstance(result, tuple):
            return [
                imath(result[0]),
                Span(['', ['answer'], []], [imath(str(result[1]))])
            ]
    if key == 'CodeBlock':
        [[ident, classes, keyvals], contents] = value
        if 'graph' in classes:
            return blatex(tikz_plot(contents, dict(keyvals), fmt))
        if 'picture' in classes:
            return blatex(tikz_picture(contents, dict(keyvals)))

if __name__ == '__main__':
    toJSONFilter(main)
