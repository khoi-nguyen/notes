from solver.helpers import latex, pre, Stf
from sympy import (
    Mul,
    Pow,
    powsimp,
    ratsimp,
    solve,
    sympify,
)


class Exercise:
    def __init__(self, transform, solve):
        self.solve = solve
        self.transform = transform

    def __call__(self, *terms):
        terms = [sympify(t, evaluate=False) for t in terms]
        exercise = self.transform(*terms)
        solution = self.display_solution(self.solve(*terms))
        return (exercise, solution)

    def display_solution(self, solution):
        if isinstance(solution, dict):
            lines = [f"{latex(key)} = {latex(val)}" for (key, val) in solution.items()]
            solution = ", ".join(lines)
        elif isinstance(solution, list):
            solution = r"\\ ".join([self.display_solution(sol) for sol in solution])
        else:
            solution = latex(solution)
        return solution


class Problem(Exercise):
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
            latex_equations.append(f"{latex(eq[0])} = {latex(eq[1])}")
        latex_equations = "\\\\ ".join(latex_equations)
        if len(equations) == 1:
            return latex_equations
        return fr"\begin{{cases}}{latex_equations}\end{{cases}}"

    def solve(self, *equations):
        system = [eq[0] - eq[1] for eq in equations]
        system = system[0] if len(system) == 1 else system
        solutions = solve(system, set=True)[1]
        if len(equations) == 1:
            return ", ".join([latex(sol[0]) for sol in solutions])
        else:
            return ", ".join([latex(sol) for sol in solutions])

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
