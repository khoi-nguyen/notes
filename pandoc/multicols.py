from pandocfilters import toJSONFilter, RawBlock, OrderedList

blatex = lambda x: RawBlock('latex', x)
bhtml = lambda x: RawBlock('html', x)

def main(key, value, fmt, meta):
    if key == 'OrderedList':
        contents = value[1]
        if len(contents) > 5 and fmt == 'beamer':
            return [blatex('\\begin{multicols}{2}')] + [OrderedList(*value)] + [blatex('\\end{multicols}')]
        elif len(contents) > 5 and fmt == 'revealjs':
            return [bhtml('<div class="multicols">')] + [OrderedList(*value)] + [bhtml('</div>')]
    if key == 'Div':
        [[ident, classes, keyvals], contents] = value
        keyvals = dict(keyvals)
        if 'n' in keyvals or 'cols' in keyvals:
            n = keyvals['n'] if 'n' in keyvals else keyvals['cols']
            return [blatex('\\begin{multicols}{' + n + '}')] + contents + [blatex('\\end{multicols}')]

if __name__ == '__main__':
    toJSONFilter(main)
