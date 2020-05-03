#!/usr/bin/env python3

from panflute import Div, OrderedList, RawBlock, run_filter


def multicols(element, document):
    if isinstance(element, OrderedList):
        if len(element.content) > 5:
            return [
                RawBlock(r"\begin{multicols}{2}", "latex"),
                element,
                RawBlock(r"\end{multicols}", "latex"),
            ]
    if isinstance(element, Div):
        attrs = element.attributes
        if "n" in attrs or "cols" in attrs:
            n = attrs["n"] if "n" in attrs else attrs["cols"]
            return [
                RawBlock(fr"\begin{{multicols}}{{{n}}}", "latex"),
                element,
                RawBlock(r"\end{multicols}", "latex"),
            ]


if __name__ == "__main__":
    run_filter(multicols)
