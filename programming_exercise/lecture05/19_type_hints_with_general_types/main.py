"""
Exercise 19: Type Hints with General Types

Goal:
    Add type hints to the functions below. Instead of committing to a single
    concrete type (like `list` or `dict`), prefer the most GENERAL type that
    still describes what the function actually needs.

Why general types?
    A function that only reads through its argument one item at a time does not
    care whether it receives a list, a tuple, a set, or a generator. If you
    annotate the parameter as `list`, you are lying about (and limiting) what
    the function accepts. Annotating it as `Iterable` tells the truth: "give me
    anything I can loop over."

Useful general types (import from `collections.abc`):
    - Iterable[T]  -> anything you can loop over once (list, tuple, set, gen...)
    - Iterator[T]  -> the result of iter(...) / a generator
    - Sequence[T]  -> supports len() and indexing (list, tuple, str, range...)
    - Mapping[K, V]-> read-only dict-like (dict, and other mappings)
    - Collection[T]-> Iterable that also supports len() and `in`
    - Hashable     -> can be used as a dict key or set element

Rule of thumb:
    Accept the most general type you can (Iterable), but return a concrete type
    (list, dict) so the caller knows exactly what they get.

How to check your type hints with mypy:
    1. Install mypy once (if you have not already):
           py -m pip install mypy
    2. Open a terminal in this folder and run:
           py -m mypy main.py

    Important: run the command from THIS folder so mypy picks up the local
    mypy.ini config file.

    If your hints are correct, mypy should report:
        Success: no issues found in 1 source file

    The local mypy.ini turns on `disallow_untyped_defs`, so mypy will complain
    until every function has full parameter and return type annotations.

TODO:
    1. Add type hints to every function parameter and return value.
    2. Use general types from `collections.abc` where appropriate.
    3. Do NOT change the function bodies.
    4. Run `py -m mypy main.py` and fix any errors until it passes.
"""

# TODO: import the general types you need from `collections.abc`
#       (see the list in the docstring above).


# TODO: `values` can be any iterable of numbers. Return a float.
def average(values):  # TODO: add parameter and return type hints
    total = 0.0
    count = 0
    for value in values:
        total += value
        count += 1
    return total / count if count else 0.0


# TODO: `items` can be any iterable of hashable elements.
#       Return a dict mapping each element to how many times it appeared.
def count_occurrences(items):  # TODO: add parameter and return type hints
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts


# TODO: `words` can be any iterable of strings.
#       Return a single string joining them with ", ".
def join_words(words):  # TODO: add parameter and return type hints
    return ", ".join(words)


# TODO: `scores` is a mapping from name (str) to score (int).
#       Return the name with the highest score.
def top_scorer(scores):  # TODO: add parameter and return type hints
    return max(scores, key=lambda name: scores[name])


# The point of this exercise: the SAME functions accept many different
# concrete types, because they were annotated with general types.

print(average([1, 2, 3, 4]))          # from a list
print(average((10, 20, 30)))          # from a tuple
print(average(x * x for x in range(5)))  # from a generator

print(count_occurrences("banana"))    # a str is iterable of characters
print(count_occurrences(["a", "b", "a", "c", "b", "a"]))

print(join_words(["red", "green", "blue"]))
print(join_words(("cat", "dog")))

print(top_scorer({"Alice": 90, "Bob": 75, "Cara": 88}))

# Expected Output:
# 2.5
# 20.0
# 6.0
# {'b': 1, 'a': 3, 'n': 2}
# {'a': 3, 'b': 2, 'c': 1}
# red, green, blue
# cat, dog
# Alice
