from pandocfilters import toJSONFilter, attributes, Math, Span, RawInline, RawBlock, Div
from environment_list import environments
import re

blatex = lambda x: RawBlock('latex', x)
ilatex = lambda x: RawInline('latex', x)
imath = lambda x: Math({'t': 'InlineMath'}, x)
answer = lambda x: [ilatex('\\answer{')] + x + [ilatex('}')]

tally = {env: 0 for env in environments}

def environment(env, ident, classes, keyvals, contents, fmt):
    global tally
    tally[env] += 1
    data = environments[env]
    title = keyvals['t'] if 't' in keyvals else ''
    if env == 'Objective' and title == '':
        title = '\\today'
    pause = '\\onslide<+->{' if fmt == 'beamer' and env != 'Code' else '{'
    begin = f"\\begin{{colorenv}}[{data['bgcolor']}]{{{data['tcolor']}}}"
    begin += f"{{{data['prefix']}\  {data['title']} {tally[env] if fmt == 'latex' else ''}}}{{{title}}}"
    end = '\\end{colorenv}}'
    keyvals = [[k, v] for k, v in keyvals.items()]
    return [blatex(pause + begin)] + [Div([ident, classes, keyvals], contents)] + [blatex(end)]

def main(key, value, fmt, meta):
    global environments
    if key == 'Span':
        [[ident, classes, keyvals], contents] = value
        if 'gap' in classes:
            return ilatex('\\vspace{' + contents[0]['c'] + '}')
        elif 'answer' in classes:
            return answer(contents)
    elif key == 'Div':
        [[ident, classes, keyvals], contents] = value
        keyvals = dict(keyvals)
        env = list(set(classes) & set(environments.keys()))
        if len(env) > 0:
            return environment(env[0], ident, classes, keyvals, contents, fmt)
    elif key == 'RawBlock' and value[0] == 'latex':
        [fmt, code] = value
        code = f'\\onslide<+->{{{code}}}'
        regex = re.compile(r'(\\plotfunction.*|\\draw.*\\draw.*)$', re.MULTILINE)
        code = re.sub(regex, r'\\onslide<+->{\1}', code)
        return RawBlock(fmt, code)

if __name__ == '__main__':
    toJSONFilter(main)
