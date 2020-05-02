import pytest
from tests.algebra import tests as algebra_tests


@pytest.mark.parametrize(
    "cmd, exercise, solution, title", algebra_tests,
)
def test_command(cmd, exercise, solution, title):
    assert cmd == (exercise, solution), title
