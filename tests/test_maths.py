import pytest
from tests.algebra import tests as algebra_tests
from tests.geometry import tests as geometry_tests


@pytest.mark.parametrize(
    "cmd, exercise, solution, title", algebra_tests,
)
def test_command(cmd, exercise, solution, title):
    assert cmd == (exercise, solution), title


@pytest.mark.parametrize("cmd, solution, title", geometry_tests)
def test_geometry(cmd, solution, title):
    assert cmd == solution, title
