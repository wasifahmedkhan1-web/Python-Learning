# Day 1 — Python Basics Revision

I’m Wasif, and this is the first day of my Python learning journey toward contributing to open source and preparing for Google Summer of Code (GSoC).

Since I already knew some Python basics, I used today to revise them and build a calculator.

## Topics Revised

- Variables and data types: integers, floats, strings, and booleans
- Input and output using `input()` and `print()`
- Checking types with `type()`
- Type conversion using `int()` and `float()`
- Arithmetic and comparison operators
- Logical operators: `and`, `or`, and `not`
- Conditional statements: `if`, `elif`, and `else`
- Loops: `for`, `while`, and `range()`
- Loop control: `break` and `continue`
- Basic string methods: `.lower()`, `.upper()`, `.strip()`, `.replace()`, and `.split()`
- Formatting output with f-strings

## Files

| File | Description |
|---|---|
| `practice.py` | Revision examples and learning notes |
| `mini_project.py` | Interactive command-line calculator |

## Mini Project — Calculator

The calculator:

- Asks for the user’s name.
- Starts when the user enters `calculator`.
- Supports addition, subtraction, multiplication, and division.
- Accepts decimal numbers.
- Checks for division by zero.
- Displays a message for unsupported operations.
- Allows repeated calculations.
- Exits when the user enters `q` after a calculation.

## How to Run

Install Python 3, then open a terminal in this folder.

Run the practice file:

```bash
python practice.py
```

Run the calculator:

```bash
python mini_project.py
```

When prompted for software, enter `calculator`.

No external packages are required.

## Learning Notes

- `input()` returns a string; numeric calculations require conversion.
- `=` assigns a value, while `==` compares values.
- Comparisons inside quotation marks are text rather than evaluated expressions.
- `and` requires both conditions to be true; `or` requires at least one.
- `break` exits a loop, while `continue` skips to its next iteration.
- Python variable names are case-sensitive: `Age` and `age` are different variables.
- `int()` truncates toward zero rather than rounding.
- `//` performs floor division; float operands can produce a float result.

## Known Limitations and Next Improvements

- Entering non-numeric text where a number is expected currently causes an error.
- Correct the division-by-zero message: division by zero is undefined, not infinity.
- Use `.strip().lower()` to handle surrounding spaces and capital letters in commands.
- Use consistent `snake_case` variable names.
- Correct remaining explanatory comments in the practice file.
- Later, organize the calculator into functions and add automated tests.

## Goal

Build a strong Python foundation, record my progress on GitHub, and gradually develop the skills needed to contribute to open-source projects.