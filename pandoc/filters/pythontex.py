#!/usr/bin/env python3

from panflute import (
    Code,
    CodeBlock,
    Math,
    RawBlock,
    RawInline,
    run_filter,
)
from pandoc.filters.helpers import context_from_pkg
from re import match
import figures.config as config
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
gl_context = {"__builtins__": None}


def surround(lines, environments):
    for env in reversed(environments):
        if isinstance(env, tuple):
            lines = [env[1](l) for l in lines]
            env = env[0]
        lines = [fr"\begin{{{env}}}", *lines, fr"\end{{{env}}}"]
    return lines


def eval_code(element, document):
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
        lines = []

        if "graph" in element.classes:
            options = {"size": 0.5, "b": -6, "l": -9, "r": 9, "t": 6}
            options.update(element.attributes)
            lines.append("{{{size}}}{{{l}}}{{{b}}}{{{r}}}{{{t}}}".format(**options))
            config.domain = "{l}:{r}".format(**options)

        for l in element.text.split("\n"):
            if match(r"^[a-zA-z_,\s]*=", l):
                exec(l, gl_context, context)
            else:
                lines.append(eval(l, gl_context, context))

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
