from pandocfilters import toJSONFilter, RawBlock, OrderedList

blatex = lambda x: RawBlock('latex', x)

def main(key, value, fmt, meta):
    if key == 'OrderedList':
        [[ident, classes, keyvals], contents] = value
        if len(contents) > 5:
            return [blatex('\\begin{multicols}{2}')] + [OrderedList(*value)] + [blatex('\\end{multicols}')]

if __name__ == '__main__':
    toJSONFilter(main)
