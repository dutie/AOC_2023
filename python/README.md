# Advent of Code 2023

Solutions and code for the Advent of Code 2023 challenges in Python.

## Introduction

This repository contains Python solutions for the Advent of Code 2023 challenges. Each day's solution is organized into a separate module within the `days` package. The main script, `main.py`, allows you to run specific days and parts, as well as perform tests.

## Getting Started

### Prerequisites

- Python 3.x

### Usage

To run a specific day and part, use the `main.py` script:

```bash
python main.py -d <day_number> -p <part_number>
```

For example, to run Day 3, Part 1:

```bash
python main.py -d 3 -p 1
```

To run tests:

```bash
python main.py -d <day_number> -p <part_number> -t 1
```

### Folder Structure

- **`days`**: Contains modules for each day's solutions.
- **inputs**: Input files for each day and part.
- **tests**: Test input and output files.

### Day Structure

Each day's solution is structured as follows:

- **`Day`** class: Abstract base class providing common functionality.
- **`parse_input`**: Method to parse input for a specific day and part.
- **`get_input`**: Method to read input from file.
- **`do_part_1`** and **`do_part_2`**: Methods to solve Part 1 and Part 2, respectively.
- **`do_test`**: Method to perform tests for a specific day and part.

### Running Tests

Tests are defined in the `tests` directory. Each test file contains input and expected output sections. Use the do_test method to run tests. Make sure to look at the examples to check how test text files are structured.

```bash
python main.py -d <day_number> -p <part_number> -t 1
```

### Performance Metrics

The `main.py` script includes timing information for each part's execution.

Happy coding!
