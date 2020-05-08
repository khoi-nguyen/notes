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
from pandoc.filters.tikz import tikz_picture
from solver.analysis import tikz_plot
from pandoc.filters.helpers import context_from_pkg

context = context_from_pkg("sympy")
context.update(context_from_pkg("solver"))
context.update(context_from_pkg("figures"))


def eval_code(element, document):
    global context
    if isinstance(element, Code):
        result = eval(element.text, globals(), context)
        if isinstance(result, (str, int, float)):
            return RawInline(str(result), "latex")
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
        if "picture" in element.classes:
            return RawBlock(tikz_picture(element.text, element.attributes), "latex")


if __name__ == "__main__":
    run_filter(eval_code)
