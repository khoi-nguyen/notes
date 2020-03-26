from pandocfilters import toJSONFilter, attributes, Math, Span, RawInline, RawBlock

blatex = lambda x: RawBlock('latex', x)
ilatex = lambda x: RawInline('latex', x)
imath = lambda x: Math({'t': 'InlineMath'}, x)
answer = lambda x, c: [ilatex('\\answer[{}]{{'.format(c))] + x + [ilatex('}')]

envcount = 1
first_env = True

# {{{
environments = {
    'Exercise': {
        'title': 'Exercise',
        'prefix': '\\faBook \\faPencil',
        'env': 'block',
    },
    'Example': {
        'title': 'Example',
        'prefix': '\\faPencilSquare',
        'env': 'exampleblock',
    },
    'Objective': {
        'title': 'Lesson Objective',
        'prefix': '\\faList\\ \\faPencilSquare',
        'env': 'block',
    },
    'Question': {
        'title': 'Question',
        'prefix': '\\faQuestionCircle',
        'env': 'block',
    },
    'Question': {
        'title': 'Question',
        'prefix': '\\faQuestionCircle',
        'env': 'block',
    },
    'Recall': {
        'title': 'Recall',
        'prefix': '\\faHistory',
        'env': 'alertblock',
    },
    'Remark': {
        'title': 'Remark',
        'prefix': '\\faPencil',
        'env': 'block',
    },
    'Solution': {
        'title': 'Solution',
        'prefix': '\\faPencilSquareO \\faCheck',
        'env': 'exampleblock',
    },
    'Theorem': {
        'title': 'Theorem',
        'prefix': '\\faBook\ \\faStar',
        'env': 'block',
    },
}
# }}}

def environment(ident, env, keyvals, contents, count):
    data = environments[env]
    title = '{}: {}'.format(data['title'], keyvals['t'] if 't' in keyvals else '')
    pause = '\\onslide<{}->{{'.format(count)
    begin = '\\begin{{{0}}}{{{1}\ {2}}}'.format(data['env'], data['prefix'], title)
    end = '\\end{{{0}}}}}'.format(data['env'])
    return [blatex(pause + begin)] + contents + [blatex(end)]

def main(key, value, fmt, meta):
    global envcount, first_env, environments
    if key == 'Span':
        envcount += 1
        [[ident, classes, keyvals], contents] = value
        return answer(contents, envcount)
    if key == 'Header' and value[0] == 1:
        envcount = 1
        first_env = True
    if key == 'Div':
        [[ident, classes, keyvals], contents] = value
        if len(set(classes) & set(environments.keys())) > 0:
            if not first_env:
                envcount += 1
            first_env = False
            return environment(ident, classes[0], dict(keyvals), contents, envcount)

if __name__ == '__main__':
    toJSONFilter(main)
