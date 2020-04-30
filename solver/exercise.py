from solver.helpers import latex, pre, Stf
from sympy import (
    Mul,
    Pow,
    powsimp,
    ratsimp,
    sympify,
)


class Exercise:
    def __init__(self, transform, solve):
        self.solve = solve
        self.transform = transform

    def __call__(self, *terms):
        terms = [sympify(t, evaluate=False) for t in terms]
        exercise = self.transform(*terms)
        solution = self.solve(*terms)
        return (exercise, latex(solution))


class EqExercise(Exercise):
    def __init__(self, solve):
        self.solve = solve

    def transform(self, lhs, rhs):
        return f"{latex(lhs)} = {latex(rhs)}"

    def __call__(self, lhs, rhs=0):
        if isinstance(lhs, str) and "=" in lhs:
            lhs, rhs = lhs.split("=")
        return super().__call__(lhs, rhs)


class OpExercise(Exercise):
    def __init__(self, op):
        self.op = op

    def transform(self, *terms):
        if self.op in ["frac", "div"]:
            terms = [latex(pre(t)) for t in terms]
            join_str = "}{" if self.op == "frac" else r" \div "
            if self.op == "div" and " " in terms[1]:
                terms[1] = fr"\br{{{terms[1]}}}"
            exercise = join_str.join(terms)
            if self.op == "frac":
                exercise = fr"\frac{{{exercise}}}"
            return exercise
        else:
            terms = [pre(t) for t in terms]
            return latex(
                self.op(*terms, evaluate=False), mul_symbol="times", order="none"
            )

    def solve(self, *terms):
        terms = [pre(t) for t in terms]
        if self.op in ["frac", "div"]:
            solution = Mul(terms[0], Pow(terms[1], -1))
        else:
            solution = self.op(*terms)
        # Simplify fractions if possible
        try:
            solution = ratsimp(solution)
        except Exception:
            pass
        return powsimp(solution)


class StfExercise(OpExercise):
    def transform(self, *terms):
        terms = [Stf(t) for t in terms]
        return super().transform(*terms)

    def solve(self, *terms):
        solution = super().solve(*terms)
        return Stf(solution)
