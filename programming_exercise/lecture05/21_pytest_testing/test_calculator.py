"""
Exercise 21: Writing Tests with pytest

Goal:
    Write automated tests for the functions in calculator.py using pytest.

What is pytest?
    pytest is a popular Python testing tool. You write small functions whose
    names start with `test_`, use plain `assert` statements, and pytest runs
    them for you and reports which ones passed or failed.

How to run your tests:
    1. Install pytest once (if you have not already):
           py -m pip install pytest
    2. Open a terminal in this folder and run:
           py -m pytest test_calculator.py -v

    If everything is correct, you should see 5 tests pass.

Expected output (your exact paths may differ slightly):
    ============================= test session starts ==============================
    ...
    test_calculator.py::test_add PASSED
    test_calculator.py::test_subtract PASSED
    test_calculator.py::test_divide PASSED
    test_calculator.py::test_divide_by_zero PASSED
    test_calculator.py::test_is_even PASSED
    ============================== 5 passed in 0.02s ===============================

Useful pytest ideas:
    - `assert result == expected`  -> fails the test if the check is wrong.
    - `pytest.raises(ErrorType)`   -> checks that code raises an exception.

Watch out:
    A test function that checks nothing still counts as PASSED. Seeing
    "5 passed" before you write any asserts does not mean you are finished --
    a real test has to be able to FAIL. Try breaking one assert on purpose
    (for example expect add(2, 3) == 6) and confirm pytest reports it.

--------------------------------------------------------------------------------
TODO:
    Fill in the five test functions below.
    Each test should call one function from calculator.py and check the result.

    1. test_add          -> add(2, 3) should be 5
    2. test_subtract     -> subtract(10, 4) should be 6
    3. test_divide       -> divide(10, 2) should be 5.0
    4. test_divide_by_zero -> divide(1, 0) should raise ZeroDivisionError
    5. test_is_even      -> is_even(4) is True, is_even(7) is False

Rules:
    - Do NOT change calculator.py.
    - Keep each function name starting with `test_` (pytest discovers them).
"""

import pytest

from calculator import add, subtract, divide, is_even


def test_add():
    # TODO: assert that add(2, 3) equals 5
    ...


def test_subtract():
    # TODO: assert that subtract(10, 4) equals 6
    ...


def test_divide():
    # TODO: assert that divide(10, 2) equals 5.0
    ...


def test_divide_by_zero():
    # TODO: check that divide(1, 0) raises ZeroDivisionError.
    # Hint: pytest.raises is used together with a `with` block.
    ...


def test_is_even():
    # TODO: assert is_even(4) is True and is_even(7) is False
    ...
