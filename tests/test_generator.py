from generator.algebra import *
from generator.analysis import *
from generator.geometry import *
from generator.helpers import pick
import pytest

exercises = [f for f in dir() if f.startswith("generate_")]


@pytest.mark.parametrize("question", exercises)
def test_generator(question):
    for level in range(1, 10):
        for i in range(0, 5):
            assert isinstance(globals()[question](level), tuple)


def test_pick():
    constraints = {
        1: ([0, 9], [0, 9], lambda a, b: (a, b) == (1, 1)),
        3: ([0, 9], [0, 9], lambda a, b: (a, b) == (3, 3)),
        5: ([5, 6, 0.5], [5, 6, 0.5], lambda a, b: a == b == 5.5),
        7: ([7, 7], [7, 7]),
        8: ([0.1, 0.9, 0.1], [0.1, 0.9, 0.1]),
    }
    assert pick(constraints, 1) == (1, 1), "Obey level's constraints"
    assert pick(constraints, 2) == (
        1,
        1,
    ), "Obey previous level's constraints when appropriate"
    assert pick(constraints, 5) == (5.5, 5.5,), "Respect range step and obey constraint"
    assert pick(constraints, 7) == (7, 7), "Ranges are closed"
    assert pick(constraints, 8)[0] * 10 in range(
        1, 10
    ), "Obey step when there are no constraints"
