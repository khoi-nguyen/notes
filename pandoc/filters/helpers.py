from pandocfilters import RawBlock, RawInline, Math


def blatex(tex):
    return RawBlock("latex", tex)


def ilatex(tex):
    return RawInline("latex", tex)


def imath(tex):
    return Math({"t": "InlineMath"}, tex)


def answer(exercise):
    return ("", exercise[1]) if isinstance(exercise, tuple) else ("", exercise)


def question(exercise):
    return exercise[0]
