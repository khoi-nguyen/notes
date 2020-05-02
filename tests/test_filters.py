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
