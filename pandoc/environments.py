from pandocfilters import toJSONFilter, Span, RawInline, RawBlock, Div
from environment_list import environments
import re

blatex = lambda x: RawBlock('latex', x)
ilatex = lambda x: RawInline('latex', x)
answer = lambda x: [ilatex('\\answer{')] + x + [ilatex('}')]

tally = {env: 0 for env in environments}

def environment(env, value, keyvals, fmt):
    global tally
    tally[env] += 1
    data = environments[env]
    title = keyvals['t'] if 't' in keyvals else ''
    pause = '\\onslide<+->{' if fmt == 'beamer' and env != 'Code' else '{'
    begin = f"\\begin{{colorenv}}[{data['bgcolor']}]{{{data['tcolor']}}}"
    begin += f"{{{data['prefix']}\  {data['title']} {tally[env] if fmt == 'latex' else ''}}}{{{title}}}"
    end = '\\end{colorenv}}'
    value[0][1].remove(env)
    return [blatex(pause + begin)] + [Div(*value)] + [blatex(end)]

def main(key, value, fmt, meta):
    if key == 'Span':
        [[ident, classes, keyvals], contents] = value
        if 'gap' in classes:
            return ilatex(f"\\vspace{{{contents[0]['c']}}}")
        elif 'answer' in classes:
            return answer(contents)
    elif key == 'Div':
        [[ident, classes, keyvals], contents] = value
        env = list(set(classes) & set(environments.keys()))
        if len(env) > 0:
            return environment(env[0], value, dict(keyvals), fmt)
    elif key == 'RawBlock' and value[0] == 'latex':
        [fmt, code] = value
        code = f'\\onslide<+->{{{code}}}'
        regex = re.compile(r'(\\plotfunction.*|\\draw.*\\draw.*)$', re.MULTILINE)
        code = re.sub(regex, r'\\onslide<+->{\1}', code)
        return RawBlock(fmt, code)

if __name__ == '__main__':
    toJSONFilter(main)
