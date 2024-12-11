import pytest

from tox_nox_python_tests.calculator import add, subtract


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (10, 5, 5),
    (-1, -1, 0),
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected
