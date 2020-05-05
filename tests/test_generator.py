from generator.algebra import *
from generator.analysis import *
from generator.geometry import *
import pytest

exercises = [f for f in dir() if f.startswith("generate_")]


@pytest.mark.parametrize("question", exercises)
def test_generator(question):
    for level in range(1, 10):
        for i in range(0, 5):
            assert isinstance(globals()[question](level), tuple)
