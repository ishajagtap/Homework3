from calculator.app import format_result, run_repl
import runpy


def test_format_result():
    assert format_result("+", 2.0, 3.0, 5.0) == "Result: 2.0 + 3.0 = 5.0"


def test_repl_exit_immediately():
    inputs = iter(["exit"])
    outputs = []

    def fake_input(prompt: str) -> str:
        return next(inputs)

    def fake_print(msg: str) -> None:
        outputs.append(msg)

    run_repl(input_fn=fake_input, output_fn=fake_print)
    assert outputs[-1] == "Goodbye!"


def test_repl_help_then_exit():
    inputs = iter(["help", "exit"])
    outputs = []

    def fake_input(prompt: str) -> str:
        return next(inputs)

    def fake_print(msg: str) -> None:
        outputs.append(msg)

    run_repl(input_fn=fake_input, output_fn=fake_print)
    assert any("Commands:" in o for o in outputs)
    assert outputs[-1] == "Goodbye!"


def test_repl_invalid_operation_then_exit():
    inputs = iter(["x", "1", "2", "exit"])
    outputs = []

    def fake_input(prompt: str) -> str:
        return next(inputs)

    def fake_print(msg: str) -> None:
        outputs.append(msg)

    run_repl(input_fn=fake_input, output_fn=fake_print)
    assert any(o.startswith("Error:") for o in outputs)
    assert outputs[-1] == "Goodbye!"


def test_repl_divide_by_zero_then_exit():
    inputs = iter(["/", "10", "0", "exit"])
    outputs = []

    def fake_input(prompt: str) -> str:
        return next(inputs)

    def fake_print(msg: str) -> None:
        outputs.append(msg)

    run_repl(input_fn=fake_input, output_fn=fake_print)
    assert any("Cannot divide by zero" in o for o in outputs)
    assert outputs[-1] == "Goodbye!"





def test_app_main_help_then_exit(monkeypatch, capsys):
    inputs = iter(["help", "exit"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Execute app as __main__
    runpy.run_module("calculator.app", run_name="__main__")

    out = capsys.readouterr().out
    assert "Commands:" in out
    assert "Goodbye!" in out


def test_repl_valid_operation_prints_result():
    inputs = iter(["+", "2", "3", "exit"])
    outputs = []

    def fake_input(prompt: str) -> str:
        return next(inputs)

    def fake_print(msg: str) -> None:
        outputs.append(msg)

    run_repl(input_fn=fake_input, output_fn=fake_print)

    # This is the line that covers app.py line 54
    assert any("Result: 2.0 + 3.0 = 5.0" in o for o in outputs)
    assert outputs[-1] == "Goodbye!"
