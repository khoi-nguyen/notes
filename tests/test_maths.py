import pytest
from tests.algebra import tests as algebra_tests
from tests.geometry import tests as geometry_tests


tests = algebra_tests + geometry_tests


def filter_by_len(tests, n):
    return [t for t in tests if len(t) == n]


@pytest.mark.parametrize("cmd, exercise, solution, title", filter_by_len(tests, 4))
def test_command(cmd, exercise, solution, title):
    assert cmd == (exercise, solution), title


@pytest.mark.parametrize("cmd, solution, title", filter_by_len(tests, 3))
def test_geometry(cmd, solution, title):
    assert cmd == solution, title
