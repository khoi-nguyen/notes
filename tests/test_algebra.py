def test_add():
    from solver.algebra import add

    assert add("1/4", "1/7") == (
        r"\frac{1}{4} + \frac{1}{7}",
        r"\frac{11}{28}",
    ), "Adding fractions"

    assert add("1/x", "1/(x + 1)") == (
        r"\frac{1}{x} + \frac{1}{x + 1}",
        r"\frac{2 x + 1}{x^{2} + x}",
    ), "Adding algebraic fractions"

    # assert add("2^4", "2^5") == ("2^{4} + 2^{5}", r"2^4 \times 3"), "Adding indices"

    # assert add("3*x + 2", "2*x + 6") == (
    #     r"\left(3 x + 2\right) + \left(2 x + 6\right)",
    #     "5 x + 8",
    # )
