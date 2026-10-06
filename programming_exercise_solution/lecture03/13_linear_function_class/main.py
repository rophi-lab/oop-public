"""
Exercise 13: Linear Function Class

Goal:
    Model a linear function f(x) = a*x + b as an object, and give it special
    methods so it can be CALLED, ADDED, MULTIPLIED, ITERATED, and SORTED like a
    built-in value.

Why this exercise?
    This is the most complete tour of Python's operator overloading. By
    implementing dunder methods you make your objects support the same syntax
    as numbers and functions. It shows how much expressive power special
    methods give you.

Special methods you will implement:
    - __call__(self, x)      -> makes the object callable: f(10) == a*10 + b.
    - __str__(self)          -> a readable string like "f(x) = 2x + 1".
    - __add__(self, other)   -> f + g, adding the a's and b's separately.
    - __mul__(self, scalar)  -> f * 2   (function on the left).
    - __rmul__(self, scalar) -> 2 * f   (number on the left; reuses __mul__).
    - __iter__(self)         -> lets you loop over the coefficients a and b.
    - __lt__(self, other)    -> compare by slope a (used for sorting).

Why both __mul__ and __rmul__?
    Python tries the LEFT operand first. For `2 * f`, the int does not know how
    to multiply by a LinearFunction, so Python falls back to f.__rmul__(2).
    Without __rmul__, `2 * f` would fail.

TODO:
    1. Implement every special method listed above.
    2. Keep the math correct (see the hints in each TODO comment).
    3. Match the Expected Output shown at the bottom of the file.
"""


class LinearFunction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"f(x) = {self.a}x + {self.b}"

    def __call__(self, x):
        return self.a * x + self.b

    def __add__(self, other):
        return LinearFunction(self.a + other.a, self.b + other.b)

    def __mul__(self, scalar):
        return LinearFunction(self.a * scalar, self.b * scalar)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __iter__(self):
        return iter((self.a, self.b))

    def __lt__(self, other):
        return self.a < other.a
    
f = LinearFunction(2, 1)
g = LinearFunction(3, 4)

print(f)
print(g)

print("f(10) =", f(10))
print("g(10) =", g(10))

h = f + g
print(h)

k = 2 * f
print(k)

print("Coefficients of f:")
for coeff in f:
    print(coeff)
functions = [
    LinearFunction(3, 4),
    LinearFunction(1, 10),
    LinearFunction(2, 1)
]

functions.sort()

print("Sorted by slope:")
for func in functions:
    print(func)

# Expected Output:
# f(x) = 2x + 1
# f(x) = 3x + 4
# f(10) = 21
# g(10) = 34
# f(x) = 5x + 5
# f(x) = 4x + 2
# Coefficients of f:
# 2
# 1
# Sorted by slope:
# f(x) = 1x + 10
# f(x) = 2x + 1
# f(x) = 3x + 4
