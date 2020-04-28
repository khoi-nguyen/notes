from random import choice, randint
from solver.geometry import pythagoras
from generator.helpers import pick
from sympy import nsimplify


def generate_pythagoras(level):
    """Pythagoras's Theorem"""
    # Generating a Pythagorean triple using Euclid's formula
    max_hypothenuse = lambda N: lambda m, n, k: k * (m ** 2 + n ** 2) <= N and m > n
    (m, n, k) = pick(
        {
            1: ([1, 9], [1, 9], [1, 9], max_hypothenuse(9)),
            3: ([1, 12], [1, 12], [1, 12], max_hypothenuse(12)),
            5: ([1, 15], [1, 15], [1, 15, 0.5], max_hypothenuse(15)),
            7: ([1, 15], [1, 15], [1, 15, 0.25], max_hypothenuse(15)),
        },
        level,
    )
    sides = [k * (m ** 2 - n ** 2), 2 * k * m * n, k * (m ** 2 + n ** 2)]
    sides = [nsimplify(s) for s in sides]

    # Replace one length by a random letter
    sides[randint(0, 2)] = choice(["a", "b", "c", "x", "y"])

    (data, solution) = pythagoras(*sides)
    return (
        "Find the missing value if a right triangle's lengths in ascending order are",
        f"{data['a']}, {data['b']}, {data['c']}",
        solution,
    )
