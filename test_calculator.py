import contextlib
import io
from pathlib import Path
import subprocess
import sys
import unittest

import calculator


class DivideTests(unittest.TestCase):
    def test_zero_divisors_return_none(self):
        for numerator in (10, 0, -3, 0.5):
            for divisor in (0, 0.0, -0.0):
                with self.subTest(numerator=numerator, divisor=divisor):
                    self.assertIsNone(calculator.divide(numerator, divisor))

    def test_nonzero_divisors_preserve_numeric_results(self):
        for a, b, expected in (
            (10, 5, 2.0), (-10, 5, -2.0), (10, -5, -2.0),
            (-10, -5, 2.0), (0, -5, 0.0), (1, 4, 0.25),
            (0.5, 0.25, 2.0), (-0.5, 0.25, -2.0),
            (1, 0.00001, 100000.0),
        ):
            with self.subTest(a=a, b=b):
                self.assertAlmostEqual(calculator.divide(a, b), expected)

    def test_other_operations_unchanged(self):
        self.assertEqual(calculator.add(-2, 0), -2)
        self.assertAlmostEqual(calculator.subtract(0.5, 0.25), 0.25)
        self.assertEqual(calculator.multiply(-3, -2), 6)


class DemoTests(unittest.TestCase):
    def test_zero_divisors_print_explanation(self):
        for a in (10, 0, -3, 0.5):
            for b in (0, 0.0, -0.0):
                with self.subTest(a=a, b=b):
                    output = io.StringIO()
                    with contextlib.redirect_stdout(output):
                        calculator.main(a, b)
                    self.assertEqual(
                        output.getvalue(),
                        f"Simple Calculator Demo\n{a} / {b} = undefined (division by zero)\n",
                    )

    def test_nonzero_divisors_print_result(self):
        for a, b, expected in ((10, 5, 2.0), (-10, 5, -2.0),
                               (10, -5, -2.0), (0.5, 0.25, 2.0),
                               (0, 5, 0.0)):
            with self.subTest(a=a, b=b):
                output = io.StringIO()
                with contextlib.redirect_stdout(output):
                    calculator.main(a, b)
                self.assertEqual(
                    output.getvalue(),
                    f"Simple Calculator Demo\n{a} / {b} = {expected}\n",
                )

    def test_script_exits_successfully_without_traceback(self):
        result = subprocess.run(
            [sys.executable, "-B", str(Path(calculator.__file__))],
            capture_output=True, text=True, timeout=10,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        self.assertEqual(
            result.stdout,
            "Simple Calculator Demo\n10 / 0 = undefined (division by zero)\n",
        )


if __name__ == "__main__":
    unittest.main()
