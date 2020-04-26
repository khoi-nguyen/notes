#!/usr/bin/env python3

from pandocfilters import toJSONFilter, RawBlock, OrderedList

blatex = lambda x: RawBlock('latex', x)

def main(key, value, fmt, meta):
    if key == 'OrderedList':
        contents = value[1]
        if len(contents) > 5:
            return [blatex('\\begin{multicols}{2}')] + [OrderedList(*value)] + [blatex('\\end{multicols}')]
    if key == 'Div':
        [[ident, classes, keyvals], contents] = value
        keyvals = dict(keyvals)
        if 'n' in keyvals or 'cols' in keyvals:
            n = keyvals['n'] if 'n' in keyvals else keyvals['cols']
            return [blatex('\\begin{multicols}{' + n + '}')] + contents + [blatex('\\end{multicols}')]

if __name__ == '__main__':
    toJSONFilter(main)
