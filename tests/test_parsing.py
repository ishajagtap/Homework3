import pytest

from calculator.operations import add
from calculator.parsing import (
    InvalidNumberError,
    InvalidOperationError,
    parse_number,
    parse_operation,
    parse_triplet,
)


@pytest.mark.parametrize("raw,expected", [("1", 1.0), ("  2.5 ", 2.5), ("-3", -3.0)])
def test_parse_number_valid(raw, expected):
    assert parse_number(raw) == expected


@pytest.mark.parametrize("raw", ["abc", "", "   ", "nan", "inf", "-inf"])
def test_parse_number_invalid(raw):
    with pytest.raises(InvalidNumberError):
        parse_number(raw)


@pytest.mark.parametrize("raw,expected_symbol", [("+", "+"), (" + ", "+"), ("*", "*")])
def test_parse_operation_valid(raw, expected_symbol):
    symbol, fn = parse_operation(raw)
    assert symbol == expected_symbol
    assert callable(fn)


@pytest.mark.parametrize("raw", ["x", "plus", "", "   "])
def test_parse_operation_invalid(raw):
    with pytest.raises(InvalidOperationError):
        parse_operation(raw)


def test_parse_triplet_ok():
    parsed = parse_triplet("+", "2", "3")
    assert parsed.op_symbol == "+"
    assert parsed.func is add
    assert parsed.a == 2.0
    assert parsed.b == 3.0
