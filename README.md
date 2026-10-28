# Hermes Agent Code Review Demo: Python Calculator

This repository contains a simple Python calculator designed specifically to demonstrate the autonomous code review capabilities of the Hermes Agent using scheduled Cron tasks. The original demo intentionally omitted error handling and tests; issue #2 adds graceful zero-division handling and automated regression coverage.

## Architecture
The application is structured as a single procedural Python script (`calculator.py`). It relies entirely on the Python standard library with no external dependencies, utilizing basic function definitions and a main execution block to output results to the standard output.

## Features
* **Basic Arithmetic Operations:** Implements core discrete functions for addition, subtraction, multiplication, and division.
* **Console Output:** Includes a built-in execution routine to print demonstration calculations directly to the terminal.
* **Graceful Zero Division:** Returns `None` for zero divisors; the demo prints an explanation instead of crashing. Regression tests cover this contract.

## Execution
To run the calculator script locally, ensure Python 3.x is installed on your system. Navigate to the repository directory and execute the following command in your terminal:

```bash
python calculator.py
```

The built-in demo uses `10 / 0`, prints `10 / 0 = undefined (division by zero)`,
and exits successfully without a traceback.

## Division contract
For integer and floating-point operands, `divide(a, b)` returns `None` when
`b == 0`, including `0`, `0.0`, and `-0.0`. This includes `0 / 0`.
Otherwise it returns Python's normal `a / b` result: negative and fractional
operands are supported, and a zero numerator with a nonzero divisor returns zero.
Callers must check `result is None` before using the result in further arithmetic;
zero is a valid result, not an error. `main(x=10, y=0)` uses this same contract to
print either the quotient or the zero-division explanation. Other invalid operand
types retain Python's normal errors; this is not a general input-validation layer.

## Tests
Run the standard-library regression suite from the repository directory:

```bash
python -B -m unittest discover -v
```

No packages are required. The tests exercise zero and signed floating zero,
negative and fractional operands, unchanged arithmetic operations, demo output,
and the script's exit status and stderr.
