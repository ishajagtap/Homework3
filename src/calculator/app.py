from __future__ import annotations

from typing import Callable

from calculator.operations import DivisionByZeroError
from calculator.parsing import (
    InvalidNumberError,
    InvalidOperationError,
    parse_triplet,
)

HELP_TEXT = """Commands:
  +  Add
  -  Subtract
  *  Multiply
  /  Divide
  help  Show this help
  exit  Quit the calculator

Example:
  Operation: +
  First number: 2
  Second number: 3
"""


def format_result(op: str, a: float, b: float, result: float) -> str:
    return f"Result: {a} {op} {b} = {result}"


def run_repl(
    input_fn: Callable[[str], str] = input,
    output_fn: Callable[[str], None] = print,
) -> None:
    output_fn("Welcome to the CLI Calculator! Type 'help' for instructions, 'exit' to quit.")

    while True:
        op_raw = input_fn("Operation (+, -, *, /) or 'help'/'exit': ").strip()

        if op_raw.lower() == "exit":
            output_fn("Goodbye!")
            return

        if op_raw.lower() == "help":
            output_fn(HELP_TEXT)
            continue

        a_raw = input_fn("First number: ")
        b_raw = input_fn("Second number: ")

        try:
            parsed = parse_triplet(op_raw, a_raw, b_raw)
            result = parsed.func(parsed.a, parsed.b)
            output_fn(format_result(parsed.op_symbol, parsed.a, parsed.b, result))
        except (InvalidOperationError, InvalidNumberError, DivisionByZeroError) as e:
            output_fn(f"Error: {e}")
            output_fn("Type 'help' to see valid commands and examples.")




if __name__ == "__main__":
    run_repl()
