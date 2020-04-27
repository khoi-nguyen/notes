def tikz_picture(contents, keyvals):
    lines = ["\\begin{center}", "\\begin{tikzpicture}"]
    for l in contents.split("\n"):
        lines.append(eval(l))
    lines += ["\\end{tikzpicture}", "\\end{center}"]
    return "\n".join(lines)


def text(label, text, x, y, options=""):
    return f"\\node[{options}] ({label}) at ({x}, {y}) {{{text}}};"


def arrow(node1, node2, options=""):
    return f"\\draw[->,{options}] ({node1}) -- ({node2});"
