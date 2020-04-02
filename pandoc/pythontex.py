from pandocfilters import toJSONFilter, attributes, Math, Span, RawInline, RawBlock, Str
from algebra import *
from analysis import *
from stats import *
from probability import *

# Shortcuts
blatex = lambda x: RawBlock('latex', x)
ilatex = lambda x: RawInline('latex', x)
imath = lambda x: Math({'t': 'InlineMath'}, x)

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
        if 'graph' in classes and fmt == 'beamer':
            return blatex(tikz_plot(contents, dict(keyvals)))

if __name__ == '__main__':
    toJSONFilter(main)
