#!/usr/bin/env python3

from panflute import (
    Code,
    CodeBlock,
    Math,
    RawBlock,
    RawInline,
    run_filter,
    Span,
    stringify,
)
from solver.algebra import *
from solver.analysis import *
from solver.stats import *
from solver.probability import *
from .tikz import *
from figures.fractions import *


def answer(x):
    return ("", x[1]) if isinstance(x, tuple) else ("", x)


def eval_code(element, document):
    if isinstance(element, Code):
        result = eval(element.text)
        if isinstance(result, (str, int, float)):
            return RawInline(str(result), "latex")
        elif isinstance(result, tuple):
            exercise, solution = str(result[0]), str(result[1])
            return [
                Math(exercise, "InlineMath"),
                Span(Math(solution, "InlineMath"), classes=["answer"]),
            ]
    if isinstance(element, CodeBlock):
        if "graph" in element.classes:
            return RawBlock(
                tikz_plot(stringify(element), element.attributes, document.format),
                "latex",
            )
        if "picture" in element.classes:
            return RawBlock(tikz_picture(element.text, element.attributes), "latex")


run_filter(eval_code)
