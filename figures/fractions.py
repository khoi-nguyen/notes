from sympy import lcm as Lcm


def text(label, text, x, y, options=""):
    return f"\\node[{options}] ({label}) at ({x}, {y}) {{{text}}};"


def arrow(node1, node2, options=""):
    return f"\\draw[->,{options}] ({node1}) -- ({node2});"


def showfrac(num, den, op=False, num2=1, den2=1):
    lines = ["\\begin{tikzpicture}"]
    lines.append("\\draw[thick] (0, 0) circle (1cm);")
    node = f"\\frac {{{num}}}{{{den}}}"
    common_den = Lcm(den, den2)
    slices = [(num, den, "fill=fraction,thick")]
    style = "thick"
    if op:
        node += f"{op}\\frac {{{num2}}}{{{den2}}}"
        if op == "+":
            slices.append((num2, -den2, "fill=fraction2,thick"))
        else:
            slices.append(
                (
                    num2,
                    den2,
                    "color=darkred,pattern=north west lines,"
                    + "pattern color=darkred,thick",
                )
            )
        if den != den2:
            style = "gray, dotted"
    slices.append((common_den, common_den, style))
    for (n, denominator, option) in slices:
        for i in range(0, n):
            angle = 90 + i * 360 / denominator
            lines.append(
                f"\\draw[{option}] (0, 0) -- ({angle}:1cm) arc"
                + f"({angle}:{angle + 360/denominator}:1cm) -- cycle;"
            )
    lines.append(f"\\node at (0, 1.5) {{${node}$}};")
    lines.append("\\end{tikzpicture}")
    return "\n".join(lines)


def rectfrac(num, den, num2=1, den2=1, side=4):
    lines = ["\\begin{tikzpicture}"]
    lines.append(f"\\draw (0, 0) rectangle ({side}, {side});")
    if num2 != 1 or den2 != 1:
        lines.append(
            f"\\draw[fill=lightblue] (0, 0) rectangle ({num/den*side}, {side});"
        )
    lines.append(
        "\\draw[thick,color=darkblue,pattern=north west lines,pattern color=darkblue]"
        + f"(0, 0) rectangle ({num/den*side}, {num2/den2*side});"
    )
    for i in range(0, den):
        lines.append(f"\\draw ({i*side/den}, 0) -- ({i*side/den}, {side});")
    for i in range(0, den2):
        lines.append(f"\\draw (0, {i*side/den2}) -- ({side}, {i*side/den2});")
    lines.append("\\end{tikzpicture}")
    return "\n".join(lines)
