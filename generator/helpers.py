from itertools import product
from random import randint, choice


def pick(constraints, level):
    """Pick random numbers satisfying a constraint depending on the level

    A constraint is a tuple consisting of ranges in which the numbers may be chosen,
    followed by a function which returns True or False depending on whether the numbers
    satisfy the constraint.

    For example ``([0, 9], [0, 9], lambda: a, b: (a + b) / 2 == 6`` is constraint which
    will force two random numbers to be between 0 and 9 and have an average of 6.

    If there is no constraint associated with the desired level, the function will have
    a look at the constraint defined in the closest lower level.

    :param contraints: A dictionary of constraints indexed by level
    :param level: integer in range(0, 10)

    Examples
    ========

    Pick a pair of numbers whose product is less than 10
    >>> pick({1: ([0, 9], [0, 9], lambda a, b: a*b < 10)}, 1)
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
            if len(range_) <= 3:
                [a, b], step = range_[:2], 1 if len(range_) <= 2 else range_[2]
                sets.append([a + n * step for n in range(0, int((b - a) // step) + 1)])
            else:
                sets.append(range_)
        solutions = [x for x in product(*sets) if callback(*x)]
        rand = choice(solutions)

    # If there are no constraints,
    # we pick numbers randomly in their respective ranges
    else:
        rand = ()
        for range_ in constraint:
            if len(range_) == 2:
                [a, b], step = range_[:2], 1 if len(range_) < 3 else range_[2]
                rand += (a + randint(0, int((b - a) // step)) * step,)
            else:
                rand += (choice(range_),)

    return rand[0] if len(rand) == 1 else rand
