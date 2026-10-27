# Hermes Agent Code Review Demo: Python Calculator

This repository contains a simple Python calculator designed specifically to demonstrate the autonomous code review capabilities of the Hermes Agent using scheduled Cron tasks. The codebase intentionally omits standard development best practices to trigger automated sub-agent feedback during live presentations.

## Architecture
The application is structured as a single procedural Python script (`calculator.py`). It relies entirely on the Python standard library with no external dependencies, utilizing basic function definitions and a main execution block to output results to the standard output.

## Features
* **Basic Arithmetic Operations:** Implements core discrete functions for addition, subtraction, multiplication, and division.
* **Console Output:** Includes a built-in execution routine to print demonstration calculations directly to the terminal.
* **Intentional Vulnerabilities:** Deliberately lacks error handling for edge cases (e.g., division by zero), explicit type hinting, and unit test coverage to serve as an effective target for LLM-based static analysis and PR review.

## Execution
To run the calculator script locally, ensure Python 3.x is installed on your system. Navigate to the repository directory and execute the following command in your terminal:

```bash
python calculator.py
