import pytest

from calculator.operations import (
    DivisionByZeroError,
    add,
    subtract,
    multiply,
    divide,
)


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (-1, 5, 4),
        (0.5, 0.25, 0.75),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (5, 2, 3),
        (2, 5, -3),
        (0.5, 0.25, 0.25),
    ],
)
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 6),
        (-2, 3, -6),
        (0.5, 0.25, 0.125),
    ],
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (6, 3, 2),
        (-6, 3, -2),
        (1, 4, 0.25),
    ],
)
def test_divide(a, b, expected):
    assert divide(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(DivisionByZeroError):
        divide(1, 0)
