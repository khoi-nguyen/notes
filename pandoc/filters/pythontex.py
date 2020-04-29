#!/usr/bin/env python3

from pandocfilters import toJSONFilter, Span
from solver.algebra import *
from solver.analysis import *
from solver.stats import *
from solver.probability import *
from .tikz import *
from figures.fractions import *
from .helpers import *


def answer(x):
    return ("", x[1]) if isinstance(x, tuple) else ("", x)


def main(key, value, fmt, meta):
    if key == "Code":
        [[ident, classes, keyvals], contents] = value
        result = eval(contents)
        if isinstance(result, (str, int, float)):
            return [ilatex(str(result))]
        elif isinstance(result, tuple):
            return [
                imath(result[0]),
                Span(["", ["answer"], []], [imath(str(result[1]))]),
            ]
    if key == "CodeBlock":
        [[ident, classes, keyvals], contents] = value
        if "graph" in classes:
            return blatex(tikz_plot(contents, dict(keyvals), fmt))
        if "picture" in classes:
            return blatex(tikz_picture(contents, dict(keyvals)))


if __name__ == "__main__":
    toJSONFilter(main)
