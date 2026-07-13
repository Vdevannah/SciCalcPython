# Scientific Calculator

An interactive, command-line calculator written in Python. The application starts in `main.py`, where you can choose an arithmetic calculator or a scientific calculator.

## Features

### Arithmetic calculator

- Addition, subtraction, multiplication, and division
- Division-by-zero handling
- Calculator display that updates after each successful operation
- Memory controls:
  - `M+` adds the displayed value to memory
  - `MC` clears memory
  - `MRC` recalls memory to the display

### Scientific calculator

Includes every arithmetic and memory feature, plus:

- Powers, square roots, and reciprocals
- Trigonometric functions: sine, cosine, and tangent
- Inverse trigonometric functions: arcsine, arccosine, and arctangent
- Trigonometric input and inverse-trigonometric results in degrees
- Base-10 and natural logarithms
- Factorials of non-negative integers
- Symbolic differentiation and integration of expressions in `x`
- Random integer generation within a supplied range
- Mean, median, and mode for a comma-separated list of numbers
- Input validation for invalid domains, such as negative square roots, zero reciprocals, and invalid logarithms

## Requirements

- Python 3
- [SymPy](https://www.sympy.org/) for symbolic differentiation and integration

## Run the application

If you are using the project virtual environment:

```bash
.venv/bin/python main.py
```

Otherwise, install the dependency in your active Python environment and run the program:

```bash
python3 -m pip install sympy
python3 main.py
```

Follow the numbered prompts to select a calculator operation. Choose **3** from the main menu to exit.

## Tests

Run the current unit-test file with:

```bash
python3 calctests.py
```
