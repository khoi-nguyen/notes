from panflute import convert_text, run_filter, stringify


def apply_filter(function, markdown):
    doc = convert_text(markdown, standalone=True)
    return run_filter(function, doc=doc)


def test_multicols():
    from pandoc.filters.multicols import multicols

    markdown = "\n".join(6 * ["#) Hello"])
    doc = apply_filter(multicols, markdown)
    assert "multicols" in stringify(
        doc
    ), "Multicols in ordered lists with more than five elements"

    markdown = "::: {.Example cols=5}\nHello\n:::"
    doc = apply_filter(multicols, markdown)
    assert "multicols}{5" in stringify(doc), "Multicols in div.env with cols attribute"

    markdown = "::: {.cols cols=3}\nHello\n:::"
    doc = apply_filter(multicols, markdown)
    assert "multicols}{3" in stringify(doc), "Multicols in div.cols"


def test_environments():
    from pandoc.filters.environments import div_to_env
    from pandoc.filters.environment_list import environments

    env, title = "Example", "Title"
    data = environments[env]

    markdown = f"::: {{.{env} t='{title}'}}\nHello\n:::"
    doc = apply_filter(div_to_env, markdown)

    assert "colorenv" in stringify(
        doc
    ), "Div with appropriate classes must become environments"
    assert data["title"] in stringify(doc), "Ensure it has become the right environment"
    assert title in stringify(doc), "Honour the t attribute"

    markdown = "[1cm]{.gap}"
    doc = apply_filter(div_to_env, markdown)
    assert "vspace" in stringify(doc), "Gap classes become vspaces"


def test_pythontex():
    from pandoc.filters.pythontex import eval_code

    markdown = "`Eq(y, Limit(sin(x)/x, x, 0, dir='+-'))`"
    doc = apply_filter(eval_code, markdown)
    assert stringify(doc).startswith(
        r"y = \lim_{x \to 0}\left(\frac{\sin{\left(x \right)}}{x}\right)"
    ), "Print sympy object as LaTeX"

    markdown = "`Expand((x - 2)*(x + 3))`"
    doc = apply_filter(eval_code, markdown)
    assert stringify(doc).startswith(r"x^{2} + x - 6"), "Print sympy object as LaTeX"

    markdown = "`equation('x^2 - 5*x + 6')`"
    doc = apply_filter(eval_code, markdown)
    assert stringify(doc).startswith(
        r"x^{2} - 5 x + 6 = 0\answer{2, 3}"
    ), "Solve exercises"

    markdown = "`2*3`"
    doc = apply_filter(eval_code, markdown)
    assert stringify(doc).startswith(r"6"), "Python evaluation"
