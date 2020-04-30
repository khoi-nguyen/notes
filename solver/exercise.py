from sympy import (
    latex as Latex,
    sympify,
)


def latex(expr, **kwargs):
    return Latex(expr, **kwargs).replace("cdot", "times")


class Exercise:
    def __init__(self, transform, solve):
        self.solve = solve
        self.transform = transform

    def export(self):
        def exercise(*terms):
            terms = [sympify(t, evaluate=False) for t in terms]
            exercise = self.transform(*terms)
            solution = self.solve(*terms)
            return (exercise, latex(solution))

        return exercise
