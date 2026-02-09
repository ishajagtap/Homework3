from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from calculator.operations import OPERATIONS


class InvalidOperationError(ValueError):
    """Raised when an operation is not recognized."""


class InvalidNumberError(ValueError):
    """Raised when a value cannot be parsed as a finite float."""


@dataclass(frozen=True)
class ParsedInput:
    op_symbol: str
    func: Callable[[float, float], float]
    a: float
    b: float


def parse_operation(op_raw: str) -> tuple[str, Callable[[float, float], float]]:
    op = op_raw.strip()
    if op not in OPERATIONS:
        raise InvalidOperationError(
            f"Invalid operation '{op_raw}'. Choose one of: {', '.join(sorted(OPERATIONS.keys()))}"
        )
    return op, OPERATIONS[op]


def parse_number(num_raw: str) -> float:
    s = num_raw.strip()
    try:
        value = float(s)
    except ValueError as e:
        raise InvalidNumberError(f"Invalid number '{num_raw}'.") from e

    # Reject NaN and infinities (robustness)
    if value != value or value in (float("inf"), float("-inf")):
        raise InvalidNumberError(f"Invalid number '{num_raw}'.")
    return value


def parse_triplet(op_raw: str, a_raw: str, b_raw: str) -> ParsedInput:
    op_symbol, func = parse_operation(op_raw)
    a = parse_number(a_raw)
    b = parse_number(b_raw)
    return ParsedInput(op_symbol=op_symbol, func=func, a=a, b=b)
