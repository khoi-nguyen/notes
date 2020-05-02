from panflute import convert_text, run_filter, stringify


def test_multicols():
    from pandoc.filters.multicols import multicols

    markdown = "\n".join(6 * ["#) Hello"])
    doc = convert_text(markdown, standalone=True)
    doc = run_filter(multicols, doc=doc)
    assert "multicols" in stringify(
        doc
    ), "Multicols in ordered lists with more than five elements"

    markdown = "::: {.Example cols=5}\nHello\n:::"
    doc = convert_text(markdown, standalone=True)
    doc = run_filter(multicols, doc=doc)
    assert "multicols}{5" in stringify(doc), "Multicols in div.env with cols attribute"

    markdown = "::: {.cols cols=3}\nHello\n:::"
    doc = convert_text(markdown, standalone=True)
    doc = run_filter(multicols, doc=doc)
    assert "multicols}{3" in stringify(doc), "Multicols in div.cols"


def test_environments():
    from pandoc.filters.environments import div_to_env
    from pandoc.filters.environment_list import environments

    env, title = "Example", "Title"
    data = environments[env]

    markdown = f"::: {{.{env} t='{title}'}}\nHello\n:::"
    doc = convert_text(markdown, standalone=True)
    doc = run_filter(div_to_env, doc=doc)

    assert "colorenv" in stringify(
        doc
    ), "Div with appropriate classes must become environments"
    assert data["title"] in stringify(doc), "Ensure it has become the right environment"
    assert title in stringify(doc), "Honour the t attribute"

    markdown = "[1cm]{.gap}"
    doc = convert_text(markdown, standalone=True)
    doc = run_filter(div_to_env, doc=doc)
    assert "vspace" in stringify(doc), "Gap classes become vspaces"
