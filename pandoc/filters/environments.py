#!/usr/bin/env python3

from panflute import Div, run_filter, RawBlock, RawInline, Span, stringify
from pandoc.filters.environment_list import environments

tally = {env: 0 for env in environments}


def environment(env, element, fmt):
    global tally
    tally[env] += 1
    data = environments[env]
    title = element.attributes["t"] if "t" in element.attributes else ""
    pause = r"\onslide<+->{" if fmt == "beamer" and env != "Code" else "{"
    begin = fr"""
        \begin{{colorenv}}[{data['bgcolor']}]{{{data['tcolor']}}}
        {{{data['prefix']}\  {data['title']} {tally[env] if fmt == 'latex' else ''}}}
        {{{title}}}
    """
    end = r"\end{colorenv}}"
    element.classes.remove(env)
    return [
        RawBlock(pause + begin, "latex"),
        element,
        RawBlock(end, "latex"),
    ]


def div_to_env(element, document):
    if isinstance(element, Span):
        if "gap" in element.classes:
            return RawInline(fr"\vspace{{{stringify(element)}}}", "latex")
    elif isinstance(element, Div):
        env = list(set(element.classes) & set(environments.keys()))
        if len(env) > 0:
            return environment(env[0], element, document.format)


if __name__ == "__main__":
    run_filter(div_to_env)
