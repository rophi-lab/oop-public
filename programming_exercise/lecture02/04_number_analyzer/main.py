"""
Exercise 04: Number Analyzer

Goal:
    Write a single function that takes a list of numbers and returns a
    dictionary summarizing them: mean, minimum, maximum, sum, count, and the
    numbers split into even and odd groups.

Why this exercise?
    Real programs rarely need just one fact about their data. Instead of
    writing five separate functions (one for the mean, one for the max, ...),
    you learn to compute several related results in one pass and return them
    together in a dictionary. A dictionary is the natural container when each
    result has a meaningful name ("mean", "count", ...).

Useful tools:
    - sum(numbers)       -> the total
    - min(numbers)       -> the smallest value
    - max(numbers)       -> the largest value
    - len(numbers)       -> how many items there are
    - a % 2 == 0         -> True when a is even
    - list comprehension -> [n for n in numbers if n % 2 == 0]

Tip:
    The mean is just sum(numbers) / len(numbers). Guard against an empty list
    if you want to be safe (dividing by zero raises an error).

TODO:
    1. Compute each value described in the docstring below.
    2. Return them all in one dictionary using the exact keys shown.
    3. Do NOT change the code that calls the function or prints the result.
"""


def analyze_numbers(numbers):
    """
    Input: A list of numbers, e.g., [1, 2, 3, 4, 5]
    Output: A dictionary with the following keys:
    - "mean": the mean of the numbers
    - "minimum": the minimum of the numbers
    - "maximum": the maximum of the numbers
    - "sum": the sum of the numbers
    - "count": the count of the numbers
    - "even_numbers": the list of even numbers
    - "odd_numbers": the list of odd numbers
    Example:
    Input: [1, 2, 3, 4, 5]
    Output: {
        "mean": 3.0,
        "minimum": 1,
        "maximum": 5,
        "sum": 15,
        "count": 5,
        "even_numbers": [2, 4],
        "odd_numbers": [1, 3, 5]
    }
    """
    # TODO: calculate each value and return the result dictionary
    return ...


numbers = [1, 2, 3, 4, 5]
print(analyze_numbers(numbers))
