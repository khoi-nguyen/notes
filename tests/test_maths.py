import pytest
from tests.algebra import tests as algebra_tests
from tests.analysis import tests as analysis_tests
from tests.geometry import tests as geometry_tests
from tests.mechanics import tests as mechanics_tests


tests = algebra_tests + analysis_tests + geometry_tests + mechanics_tests


def filter_by_len(tests, n):
    return [t for t in tests if len(t) == n]


@pytest.mark.parametrize("cmd, exercise, solution, title", filter_by_len(tests, 4))
def test_command(cmd, exercise, solution, title):
    assert cmd == (exercise, solution), title


@pytest.mark.parametrize("cmd, solution, title", filter_by_len(tests, 3))
def test_geometry(cmd, solution, title):
    assert cmd == solution, title


def test_conflicts():
    count = {"expand": 0, "integrate": 0, "simplify": 0}
    modules = ["algebra", "analysis", "geometry", "mechanics"]
    for module in modules:
        exec(f"import solver.{module}")
        for function in count:
            if eval(f"hasattr(solver.{module}, '{function}')"):
                count[function] += 1

    for function, count in count.items():
        assert count == 1, f"Potential conflict with {function}"
