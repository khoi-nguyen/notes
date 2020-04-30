from sympy import (
    latex as Latex,
    Mul,
    Pow,
    powsimp,
    Symbol,
    sympify,
    UnevaluatedExpr,
)


def latex(expr, **kwargs):
    return Latex(expr, **kwargs).replace("cdot", "times")


# Specify which simplifications we allow
# e.g. allow multiplications but don't touch power bases
def pre(term, level=0):
    args = [pre(a, level + 1) for a in term.args]
    if term.func == Mul:
        term = Mul(*args, evaluate=True)
    if term.func == Pow and not level:
        [base, power] = args
        # Ensure this is not a fraction with numerator 1
        if base.func != Symbol and power != -1:
            term = Pow(UnevaluatedExpr(args[0]), args[1])
    return term


class Exercise:
    def __init__(self, transform, solve):
        self.solve = solve
        self.transform = transform

    def __call__(self, *terms):
        terms = [sympify(t, evaluate=False) for t in terms]
        exercise = self.transform(*terms)
        solution = self.solve(*terms)
        return (exercise, latex(solution))


class OpExercise(Exercise):
    def __init__(self, op):
        self.op = op

    def transform(self, *terms):
        terms = [pre(t) for t in terms]
        return latex(self.op(*terms, evaluate=False), mul_symbol="times", order="none")

    def solve(self, *terms):
        terms = [pre(t) for t in terms]
        return powsimp(self.op(*terms))
