import pytest
from solver.algebra import (
    add,
    circle_equation,
    div,
    equation,
    mult,
    round,
    subtract,
    stf,
    stfadd,
    stf2dec,
    stfdiv,
    stffrac,
    stfmult,
    stfsub,
)
from sympy import expand as Expand


# assert add("2^4", "2^5") == ("2^{4} + 2^{5}", r"2^4 \times 3"), "Adding indices"

# assert add("3*x + 2", "2*x + 6") == (
#     r"\left(3 x + 2\right) + \left(2 x + 6\right)",
#     "5 x + 8",
# )


@pytest.mark.parametrize(
    "cmd, exercise, solution, title",
    [
        (
            add("1/4", "1/7"),
            r"\frac{1}{4} + \frac{1}{7}",
            r"\frac{11}{28}",
            "Adding fractions",
        ),
        (
            add("1/x", "1/(x + 1)"),
            r"\frac{1}{x} + \frac{1}{x + 1}",
            r"\frac{2 x + 1}{x^{2} + x}",
            "Adding algebraic fractions",
        ),
        (
            subtract("1/4", "1/7"),
            r"\frac{1}{4} - \frac{1}{7}",
            r"\frac{3}{28}",
            "Subtracting fractions",
        ),
        (
            subtract("1/x", "1/(x + 1)"),
            r"\frac{1}{x} - \frac{1}{x + 1}",
            r"\frac{1}{x^{2} + x}",
            "Subtracting algebraic fractions",
        ),
        (mult("4^2", "4^3"), r"4^{2} \times 4^{3}", "4^{5}", "Index multiplication"),
        (
            mult("4^2", "4^1"),
            r"4^{2} \times 4",
            "4^{3}",
            "Index multiplication with power 1",
        ),
        (
            mult("y^k", "y^3"),
            r"y^{k} \times y^{3}",
            "y^{k + 3}",
            "Index multiplication (letter for base and power)",
        ),
        (
            div("3^7", "3^2"),
            r"3^{7} \div 3^{2}",
            "3^{5}",
            "Index division with integers",
        ),
        (
            div("y^k", "y^3"),
            r"y^{k} \div y^{3}",
            "y^{k - 3}",
            "Index division (letter for base and power)",
        ),
        (
            div("-3*x^3", "x^2"),
            r"- 3 x^{3} \div x^{2}",
            "- 3 x",
            "Avoid unnecessary bracket around negative numbers",
        ),
        (equation("3*x + 4 = 10"), "3 x + 4 = 10", "2", "Solving linear equation",),
        (
            equation("x^2 - 5*x + 6"),
            "x^{2} - 5 x + 6 = 0",
            "2, 3",
            "Quadratic equation equals 0 by default",
        ),
        (
            equation(Expand("(x - 4)*(x + 3)")),
            "x^{2} - x - 12 = 0",
            "-3, 4",
            "Quadratic equation from factorised form",
        ),
        (round(1.73666, 2), "1.73666", "1.74", "Rounding to 2 dp",),
        (round(3456, sf=2), "3456", "3500", "Rounding to 2 sf",),
        (round(9999, sf=1), "9999", "10000", "Rounding to 1 sf with nines",),
        (stf(485), "485", r"4.85 \times 10^{2}", "Standard form (bigger than 1)",),
        (stf(0.0032), "0.0032", r"3.2 \times 10^{-3}", "Standard form (less than 1)",),
        (stf(0.00312), "0.00312", r"3.12 \times 10^{-3}", "Standard form (rounding)",),
        (
            stf(0.002),
            "0.002",
            r"2 \times 10^{-3}",
            "Standard form (one significant figure)",
        ),
        (
            stf(-0.00352),
            "-0.00352",
            r"- 3.52 \times 10^{-3}",
            "Standard form (negative number)",
        ),
        (
            stf(5.4 * 10 ** 4),
            "54000",
            r"5.4 \times 10^{4}",
            "Standard form with standard form notation",
        ),
        (
            stf(1.47 * 10 ** -7),
            "0.000000147",
            r"1.47 \times 10^{-7}",
            "Standard form with standard form notation",
        ),
        (
            stf("1.47 * 10^-7"),
            "0.000000147",
            r"1.47 \times 10^{-7}",
            "Standard form with Sympy expression",
        ),
        (
            stf2dec(-0.00352),
            r"- 3.52 \times 10^{-3}",
            "-0.00352",
            "Standard form to decimal",
        ),
        (
            stfmult(40000, 0.01),
            r"4 \times 10^{4} \times 10^{-2}",
            r"4 \times 10^{2}",
            "Standard form multiplication",
        ),
        (
            stffrac(10000, 0.2),
            r"\frac{10^{4}}{2 \times 10^{-1}}",
            r"5 \times 10^{4}",
            "Standard form division (frac)",
        ),
        (
            stfdiv(10000, 0.2),
            r"10^{4} \div \br{2 \times 10^{-1}}",
            r"5 \times 10^{4}",
            "Standard form division (div)",
        ),
        (
            stfadd(10000, 2000),
            r"10^{4} + 2 \times 10^{3}",
            r"1.2 \times 10^{4}",
            "Standard form addition",
        ),
        (
            stfsub(10000, 2000),
            r"10^{4} - 2 \times 10^{3}",
            r"8 \times 10^{3}",
            "Standard form subtraction",
        ),
        (
            circle_equation("radius", "x^2 + y^2 - 16 = 9"),
            "x^{2} + y^{2} - 16 = 9",
            "5",
            "Radius of a circle with RHS",
        ),
        (
            circle_equation("radius", "(x - 3)^2 + (y + 5)^2 = 16"),
            r"\left(x - 3\right)^{2} + \left(y + 5\right)^{2} = 16",
            "4",
            "Radius of a circle with canonical LHS",
        ),
        (
            circle_equation("radius", Expand("3*((x - 2)**2 + (y + 1)**2 - 4)")),
            "3 x^{2} - 12 x + 3 y^{2} + 6 y + 3 = 0",
            "2",
            "Radius of a circle without rhs",
        ),
        (
            circle_equation("center", Expand("(x - 3)**2 + (y - 1)**2 - 16")),
            "x^{2} - 6 x + y^{2} - 2 y - 6 = 0",
            r"\br{3, 1}",
            "Center of a circle with rhs",
        ),
        (
            circle_equation("center", "(x - 3)^2 + (y + 5)^2 = 16"),
            r"\left(x - 3\right)^{2} + \left(y + 5\right)^{2} = 16",
            r"\br{3, -5}",
            "Center of a circle with factorised lhs",
        ),
        (
            circle_equation("center", Expand("3*((x - 2)**2 + (y + 1)**2 - 4)")),
            "3 x^{2} - 12 x + 3 y^{2} + 6 y + 3 = 0",
            r"\br{2, -1}",
            "Center of a circle without rhs",
        ),
    ],
)
def test_command(cmd, exercise, solution, title):
    assert cmd == (exercise, solution), title
