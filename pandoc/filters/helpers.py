from pandocfilters import RawBlock, RawInline, Math


def blatex(tex):
    return RawBlock("latex", tex)


def ilatex(tex):
    return RawInline("latex", tex)


def answer(tex):
    return [ilatex("\\answer{")] + tex + [ilatex("}")]


def imath(tex):
    return Math({"t": "InlineMath"}, tex)


def question(exercise):
    return exercise[0]
