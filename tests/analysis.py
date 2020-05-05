from solver.analysis import (
    diff,
    gradient,
    integrate,
    line_equation,
    maximum,
    minimum,
    plot,
    showsecant,
    showtangent,
    stationary,
    tangent,
    taylor,
    taylor_poly,
    tikz_plot,
)

tests = [
    # Plots
    (
        plot("x"),
        r"\plotfunction[darkblue]{-9:9}{(\x)}",
        r"Check x is replaced by \x in \plot",
    ),
    (
        plot("x**2"),
        r"\plotfunction[darkblue]{-9:9}{(\x)^2}",
        r"Check ** is replaced by ^ in \plot",
    ),
    (
        plot("x", "darkred"),
        r"\plotfunction[darkred]{-9:9}{(\x)}",
        "Changing plot color",
    ),
    (
        plot("x", "darkred", "3:4"),
        r"\plotfunction[darkred]{3:4}{(\x)}",
        "Changing plot domain",
    ),
    (
        plot("sin(x)"),
        r"\plotfunction[darkblue]{-9:9}{sin(((\x))r)}",
        "Force use of radians for plots",
    ),
    (
        plot("sin(cos(x))"),
        r"\plotfunction[darkblue]{-9:9}{sin((cos(((\x))r))r)}",
        "Radians in nested trig functions for plots",
    ),
    (
        showtangent("sin(x)", 0),
        r"\plotfunction[darkgreen]{-9:9}{(\x)}",
        "Show tangent of a function at a point",
    ),
    (
        showsecant("x^2", 0, 1),
        r"\plotfunction[darkred]{-9:9}{(\x)}",
        "Show secant of a function at a point",
    ),
    # Tikz
    (
        tikz_plot("plot('x')", {"l": -2, "r": 2, "b": -3, "t": 4}, 0).replace("\n", ""),
        r"{\begin{plot}{0.5}{-2}{-3}{2}{4}"
        + r"\plotfunction[darkblue]{-2:2}{(\x)}\end{plot}}",
        "Tikz grid",
    ),
    (
        tikz_plot("f = 0\nplot(f)", {"l": -2, "r": 2, "b": -3, "t": 4}, 0).replace(
            "\n", ""
        ),
        r"{\begin{plot}{0.5}{-2}{-3}{2}{4}"
        + r"\plotfunction[darkblue]{-2:2}{0}\end{plot}}",
        "Tikz grid",
    ),
    (gradient(0, 0, 1, 2)[1], "2", "Gradient from two points",),
    (
        line_equation(3, 1, 2)[1],
        "y = 3 x - 1",
        "Find the line equation with gradient and point",
    ),
    (
        line_equation(0, 1, 1, 3)[1],
        "y = 2 x + 1",
        "Find the line equation with two points",
    ),
    # Differentiation
    (
        diff("x^n"),
        r"\frac{d}{d x} x^{n}",
        "n x^{n - 1}",
        "Treat other variables as constant when differentiating",
    ),
    (
        diff("x*y", "x", partial=True)[0],
        r"\frac{\partial}{\partial x} x y",
        "Partial differentiation",
    ),
    (
        diff("sin(x)^2")[1],
        r"2 \sin{\left(x \right)} \cos{\left(x \right)}",
        "Don't factorise trig functions",
    ),
    # Tangents
    (
        tangent("x^2", 1),
        r"y = x^{2} \text{ at } x = 1",
        "y = 2 x - 1",
        "Tangent of a function at a point",
    ),
    # Integration
    (
        integrate("x^2", 0, 1),
        r"\int\limits_{0}^{1} x^{2}\, dx",
        r"\frac{1}{3}",
        "Integrate with bounds",
    ),
    (
        integrate("x^2"),
        r"\int x^{2}\, dx",
        r"\frac{x^{3}}{3}",
        "Integrate without bounds",
    ),
    # Taylor
    (
        str(taylor("exp(x)", 0, 3)),
        "x**3/6 + x**2/2 + x + 1",
        "Taylor development at a point in symbolic form",
    ),
    (
        taylor_poly("sin(x)", 0, 3),
        r"- \frac{x^{3}}{6} + x",
        "Taylor polynomial of a function at a point",
    ),
    # Stationary points
    (
        stationary("x^2 - 6*x + 4"),
        "x^{2} - 6 x + 4",
        r"\left\{3\right\}",
        "Stationary points",
    ),
    # Minimum
    (minimum("x^2 + 4*x + 6"), "x^{2} + 4 x + 6", "-2", "Single minimum function",),
    (
        minimum("(x-2)^2 * (x-3)^2"),
        r"\left(x - 3\right)^{2} \left(x - 2\right)^{2}",
        "2, 3",
        "Double minimum function",
    ),
    # Maximum
    (
        maximum("-(x - 2)^2 * (x + 3)^2"),
        r"\left(x - 2\right)^{2} \left(x + 3\right)^{2}",
        "-3, 2",
        "Find function max",
    ),
]
