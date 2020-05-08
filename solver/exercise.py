from solver.helpers import latex, pre, Stf
from sympy import (
    Eq,
    Mul,
    Pow,
    powsimp,
    ratsimp,
    solve,
    sympify,
)


class Exercise:
    join = ", "
    join2 = r"\\ "

    show_exercise = True

    def __init__(self, transform=False, solve=False, join=False):
        self.solve = solve
        if transform:
            self.transform = transform
        if join:
            self.join = join

    def __call__(self, *terms):
        terms = [sympify(t, evaluate=False) for t in terms]
        exercise = self.display(self.transform(*terms)) if self.show_exercise else ""
        terms = self.presolve(*terms)
        solution = self.display(self.solve(*terms))
        return (exercise, solution)

    def presolve(self, *terms):
        return terms

    def display(self, solution):
        if isinstance(solution, dict):
            lines = [latex(Eq(key, val)) for (key, val) in solution.items()]
            solution = self.join.join(lines)
        elif isinstance(solution, list):
            use_newline = True in [isinstance(s, (list, dict)) for s in solution]
            join_char = self.join2 if use_newline else self.join
            solution = join_char.join([self.display(sol) for sol in solution])
        else:
            solution = latex(solution)
        return solution

    def transform(self, *terms):
        return self.join.join([latex(t) for t in terms])


class Problem(Exercise):
    show_exercise = False

    def __init__(self, solve):
        self.solve = solve
        self.transform = lambda *params: locals()


class EqExercise(Exercise):
    def __init__(self, solve=False):
        if solve:
            self.solve = solve

    def transform(self, *equations):
        latex_equations = []
        for eq in equations:
            latex_equations.append(latex(Eq(eq[0], eq[1])))
        latex_equations = "\\\\ ".join(latex_equations)
        if len(equations) == 1:
            return latex_equations
        return fr"\begin{{cases}}{latex_equations}\end{{cases}}"

    def presolve(self, *equations):
        return [eq[0] - eq[1] for eq in equations]

    def solve(self, *equations):
        solutions = solve(equations, set=True)[1]
        if len(equations) == 1:
            return self.join.join([latex(sol[0]) for sol in solutions])
        else:
            return self.join.join([latex(sol) for sol in solutions])

    def __call__(self, *equations):
        args = []
        for eq in equations:
            if isinstance(eq, str) and "=" in eq:
                lhs, rhs = eq.split("=")
            else:
                lhs, rhs = eq, 0
            args.append([lhs, rhs])
        return super().__call__(*args)


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
