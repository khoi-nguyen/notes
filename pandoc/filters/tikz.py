from pandoc.filters.helpers import context_from_pkg

context = context_from_pkg("solver")
context.update(context_from_pkg("figures"))


def tikz_picture(contents, keyvals):
    global context
    lines = ["\\begin{center}", "\\begin{tikzpicture}"]
    for l in contents.split("\n"):
        lines.append(eval(l, globals(), context))
    lines += ["\\end{tikzpicture}", "\\end{center}"]
    return "\n".join(lines)
