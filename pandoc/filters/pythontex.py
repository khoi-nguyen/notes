#!/usr/bin/env python3

from panflute import (
    Code,
    CodeBlock,
    Math,
    RawBlock,
    RawInline,
    run_filter,
    stringify,
)
from pandoc.filters.helpers import context_from_pkg
from solver.analysis import tikz_plot
import sympy

context = {f: getattr(sympy, f) for f in dir(sympy) if not f.startswith("_")}
context.update(context_from_pkg("solver"))
context.update(context_from_pkg("figures"))
context.update(
    {
        "h": sympy.Symbol("h", real=True),
        "n": sympy.Symbol("n", integer=True, nonnegative=True),
        "t": sympy.Symbol("t", real=True),
        "x": sympy.Symbol("x", real=True),
        "y": sympy.Symbol("y", real=True),
    }
)


def surround(lines, environments):
    for env in reversed(environments):
        if isinstance(env, tuple):
            lines = [env[1](l) for l in lines]
            env = env[0]
        lines = [fr"\begin{{{env}}}", *lines, fr"\end{{{env}}}"]
    return lines


def eval_code(element, document):
    global context
    if isinstance(element, Code):
        result = eval(element.text, globals(), context)
        if isinstance(result, (str, int, float)):
            return RawInline(str(result), "latex")
        elif isinstance(result, sympy.Basic):
            return RawInline(sympy.latex(result), "latex")
        elif isinstance(result, tuple):
            exercise, solution = str(result[0]), str(result[1])
            return [
                Math(exercise, "InlineMath"),
                RawInline(r"\answer{", "latex"),
                Math(solution, "InlineMath"),
                RawInline("}", "latex"),
            ]
    if isinstance(element, CodeBlock):
        if "graph" in element.classes:
            return RawBlock(
                tikz_plot(stringify(element), element.attributes, document.format),
                "latex",
            )

        # Evaluate
        lines = []
        for l in element.text.split("\n"):
            lines.append(eval(l, globals(), context))

        # Surround by the appropriate environments
        extra_environments = {
            "graph": ["plot"],
            "picture": ["center", "tikzpicture"],
            "equation": [("align*", sympy.latex)],
        }
        for code_class in element.classes:
            if code_class in extra_environments:
                lines = surround(lines, extra_environments[code_class])

        return RawBlock("\n".join(lines), "latex")


if __name__ == "__main__":
    run_filter(eval_code)
