from sympy import Abs, Add, floor, latex as Latex, log, Mul, Pow, UnevaluatedExpr


def display_float(number):
    return f"{number.evalf():.15f}".rstrip("0").rstrip(".")


def latex(expr, **kwargs):
    return Latex(expr, **kwargs).replace("cdot", "times")


def Subtract(a, b, **kwargs):
    return Add(a, Mul(-1, b), **kwargs)


def Stf(number):
    """Converts a float to standard notation as a sympy object
    """
    power = floor((log(Abs(number)) / log(10)).evalf())
    x = Mul(number, Pow(10, -power)).evalf()
    if float(x).is_integer():
        x = int(x)
    return Mul(x, Pow(UnevaluatedExpr(10), power, evaluate=False), evaluate=False)
