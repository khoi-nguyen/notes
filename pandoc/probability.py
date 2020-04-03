from sympy import binomial, latex

def binom(n, k):
    exercise = f"\\binom {{{n}}} {{{k}}}"
    solution = latex(binomial(n, k))
    return (exercise, solution)
