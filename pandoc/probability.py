from sympy.stats import Normal, Binomial, Poisson, cdf
from sympy import binomial, latex, sympify, evalf

def binom(n, k):
    exercise = f"\\binom {{{n}}} {{{k}}}"
    solution = latex(binomial(n, k))
    return (exercise, solution)

def normal(a, b, mu = 0, sigma = 1):
    exercise = f"P({latex(sympify(a))} < X < {latex(sympify(b))})"
    X = Normal("X", mu, sigma)
    solution = cdf(X)(b) - cdf(X)(a)
    solution = solution.evalf().round(3)
    return (exercise, solution)

def bin(a, b, n, p):
    exercise = f"P({latex(sympify(a))} < X < {latex(sympify(b))})"
    X = Binomial("X", n, p)
    solution = cdf(X)[b] - cdf(X)[a]
    solution = solution.evalf().round(3)
    return (exercise, solution)

def poisson(a, b, k, l):
    exercise = f"P({latex(sympify(a))} < X < {latex(sympify(b))})"
    X = Poisson("X", l)
    solution = cdf(X)(b) - cdf(X)(a)
    solution = solution.evalf().round(3)
    return (exercise, solution)
