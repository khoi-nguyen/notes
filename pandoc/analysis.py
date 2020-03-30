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
