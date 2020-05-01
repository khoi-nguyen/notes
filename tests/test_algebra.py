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


def test_subtract():
    from solver.algebra import subtract

    assert subtract("1/4", "1/7") == (
        r"\frac{1}{4} - \frac{1}{7}",
        r"\frac{3}{28}",
    ), "Subtracting fractions"

    assert subtract("1/x", "1/(x + 1)") == (
        r"\frac{1}{x} - \frac{1}{x + 1}",
        r"\frac{1}{x^{2} + x}",
    ), "Subtracting algebraic fractions"


def test_mult():
    from solver.algebra import mult

    assert mult("4^2", "4^3") == (
        r"4^{2} \times 4^{3}",
        "4^{5}",
    ), "Index multiplication"

    assert mult("4^2", "4^1") == (
        r"4^{2} \times 4",
        "4^{3}",
    ), "Index multiplication with power 1"

    assert mult("y^k", "y^3") == (
        r"y^{k} \times y^{3}",
        "y^{k + 3}",
    ), "Index multiplication (letter for base and power)"


def test_div():
    from solver.algebra import div

    assert div("3^7", "3^2") == (
        r"3^{7} \div 3^{2}",
        "3^{5}",
    ), "Index division with integers"

    assert div("y^k", "y^3") == (
        r"y^{k} \div y^{3}",
        "y^{k - 3}",
    ), "Index division (letter for base and power)"

    assert div("-3*x^3", "x^2") == (
        r"- 3 x^{3} \div x^{2}",
        "- 3 x",
    ), "Avoid unnecessary bracket around negative numbers"


def test_equation():
    from solver.algebra import equation, Expand

    assert equation("3*x + 4 = 10") == ("3 x + 4 = 10", "2"), "Solving linear equation"

    assert equation("x^2 - 5*x + 6") == (
        "x^{2} - 5 x + 6 = 0",
        "2, 3",
    ), "Quadratic equation equals 0 by default"

    assert equation(Expand("(x - 4)*(x + 3)")) == (
        "x^{2} - x - 12 = 0",
        "-3, 4",
    ), "Quadratic equation from factorised form"


def test_stf():
    from solver.algebra import stf

    assert stf(485) == ("485", r"4.85 \times 10^{2}"), "Standard form (bigger than 1)"

    assert stf(0.0032) == (
        "0.0032",
        r"3.2 \times 10^{-3}",
    ), "Standard form (less than 1)"

    assert stf(0.00312) == (
        "0.00312",
        r"3.12 \times 10^{-3}",
    ), "Standard form (rounding)"

    assert stf(0.002) == (
        "0.002",
        r"2 \times 10^{-3}",
    ), "Standard form (one significant figure)"

    assert stf(-0.00352) == (
        "-0.00352",
        r"- 3.52 \times 10^{-3}",
    ), "Standard form (negative number)"

    assert stf(5.4 * 10 ** 4) == (
        "54000",
        r"5.4 \times 10^{4}",
    ), "Standard form with standard form notation"

    assert stf(1.47 * 10 ** -7) == (
        "0.000000147",
        r"1.47 \times 10^{-7}",
    ), "Standard form with standard form notation"

    assert stf("1.47 * 10^-7") == (
        "0.000000147",
        r"1.47 \times 10^{-7}",
    ), "Standard form with Sympy expression"
