from itertools import product
from random import randint, choice


def pick(constraints, level):
    """Pick random solution of a constraint that depends on level

    :param contraints:
    :param level: integer in range(0, 10)
    """

    # Select the appropriate contstraint
    level = max([n for n in constraints.keys() if n <= level])
    constraint = constraints[level]

    # Technically, constraints should always be tuples.
    # We allow lists for readability
    # when there's only one number to pick
    if isinstance(constraint, list):
        constraint = (constraint,)

    # If there are constraints, we choose a random solution
    # amongst all possibilities
    if callable(constraint[-1]):
        callback = constraint[-1]
        sets = []
        for range_ in constraint[:-1]:
            [a, b], step = range_[:2], 1 if len(range_) <= 2 else range_[2]
            sets.append([a + n * step for n in range(0, int((b - a) // step) + 1)])
        solutions = [x for x in product(*sets) if callback(*x)]
        rand = choice(solutions)

    # If there are no constraints,
    # we pick numbers randomly in their respective ranges
    else:
        rand = ()
        for range_ in constraint:
            [a, b], step = range_[:2], 1 if len(range_) < 3 else range_[2]
            rand += (a + randint(0, int((b - a) // step)) * step,)

    return rand[0] if len(rand) == 1 else rand
