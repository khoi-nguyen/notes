from solver.exercise import VectorProblem
from sympy import integrate as Integrate, solve, symbols


def motion(t0="t_0", x0="x_0", v0="v_0", T="T", X="x_T", V="v_T", a="a", n=1):
    def solution(t0, x0, v0, T, X, V, a):
        s, t = symbols("s t")
        velocity = [v0[i] + Integrate(a[i].subs(t, s), (s, t0, t)) for i in range(n)]
        position = [
            x0[i] + Integrate(velocity[i].subs(t, s), (s, t0, t)) for i in range(n)
        ]
        equations = [position[i].subs(t, T) - X[i] for i in range(n)] + [
            velocity[i].subs(t, T) - V[i] for i in range(n)
        ]
        return solve(equations, dict=True)

    return VectorProblem(solution, dim=n, vectors=[1, 2, 4, 5, 6])(
        t0, x0, v0, T, X, V, a
    )
