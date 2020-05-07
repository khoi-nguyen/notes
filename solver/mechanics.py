from solver.exercise import Problem
from sympy import integrate as Integrate, solve, symbols


def motion(t0="t_0", x0="x_0", v0="v_0", T="T", X="x_T", V="v_T", a="a"):
    def solution(t0, x0, v0, T, X, V, a):
        s, t = symbols("s t")
        velocity = v0 + Integrate(a.subs(t, s), (s, t0, t))
        position = x0 + Integrate(velocity.subs(t, s), (s, t0, t))
        equations = [position.subs(t, T) - X, velocity.subs(t, T) - V]
        return solve(equations)

    return Problem(solution)(t0, x0, v0, T, X, V, a)
