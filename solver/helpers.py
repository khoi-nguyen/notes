from decimal import Decimal, ROUND_HALF_UP
from sympy import (
    Abs,
    Add,
    floor,
    latex as Latex,
    log,
    Mul,
    Pow,
    Symbol,
    UnevaluatedExpr,
)


def display_float(number):
    return f"{number.evalf():.15f}".rstrip("0").rstrip(".")


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


def Subtract(a, b, **kwargs):
    return Add(a, Mul(-1, b), **kwargs)


def Round(number, dp=0, sf=False):
    x, power, n = number, 0, dp
    if sf:
        (x, power) = Stf(number, True)
        n = sf - 1
    x = Decimal(str(x)).quantize(Decimal("0.1") ** n, rounding=ROUND_HALF_UP)
    x = Mul(x, Pow(10, power)).evalf()
    if float(x).is_integer():
        x = int(x)
    return x


def Stf(number, return_tuple=False):
    """Converts a float to standard notation as a sympy object
    """
    power = floor((log(Abs(number)) / log(10)).evalf())
    x = Mul(number, Pow(10, -power)).evalf()
    if float(x).is_integer():
        x = int(x)
    if return_tuple:
        return (x, power)
    return Mul(x, Pow(UnevaluatedExpr(10), power, evaluate=False), evaluate=False)
