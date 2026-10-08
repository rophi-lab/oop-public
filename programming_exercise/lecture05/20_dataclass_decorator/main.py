"""
Exercise 20: The @dataclass Decorator

Goal:
    Use Python's `@dataclass` decorator to build classes that store data without
    writing __init__ by hand. Practice two handy features:
        1. `__post_init__`  -> run a little code AFTER the auto __init__.
        2. `field(default_factory=list)` -> a safe default EMPTY list.

What does @dataclass do for you?
    Put `@dataclass` above a class and just list the fields with type hints.
    Python then writes these for you automatically:
        - __init__   (takes the fields as arguments, in order)
        - __repr__   (prints like "ClassName(field=value, ...)")
        - __eq__     (two objects are equal if all their fields are equal)

The mutable default trap (why we need default_factory):
    You might expect to write `hobbies: list = []` to default to an empty list.
    But that ONE list would be shared by every object you create (a common bug!),
    so Python refuses to run it. The fix is the `field()` helper with its
    `default_factory` option: you hand it something that BUILDS a fresh empty
    container each time an object is created. For a list, that builder is just
    the `list` type itself.

--------------------------------------------------------------------------------
TODO 1: `Point`
    Turn it into a dataclass with two fields: x and y, both int.
    Do NOT write __init__, __repr__, or __eq__ yourself.

TODO 2: `Person`
    Turn it into a dataclass with three fields:
        - name, a str
        - age, an int
        - hobbies, a list that starts out EMPTY for every new Person
          (see the mutable default trap above)
    Then write `__post_init__(self)` so it prints a greeting, for example:
        "Hi, I'm Alice and I'm 30 years old."

Rules:
    - Do NOT write your own __init__, __repr__, or __eq__.
    - Do NOT change the code below the "DO NOT EDIT" line.
"""

# TODO: import the two names you need from the `dataclasses` module.


# TODO 1: mark this class as a dataclass, then give each field its type.
class Point:
    x: ...
    y: ...


# TODO 2: mark this class as a dataclass. Give name and age their types, and
#         give hobbies a default that produces a NEW empty list per object.
class Person:
    name: ...
    age: ...
    hobbies: ...

    def __post_init__(self):
        # TODO: print a greeting built from self.name and self.age.
        pass


# ------------------------------- DO NOT EDIT -------------------------------- #

# Point: free __init__, __repr__ and __eq__
p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1)                 # uses the auto __repr__
print(p1 == p2)           # True -> auto __eq__ compares the fields

# Person: __post_init__ runs automatically, hobbies starts as its own empty list
alice = Person("Alice", 30)
bob = Person("Bob", 25)
alice.hobbies.append("reading")
print(alice.hobbies)      # ['reading']
print(bob.hobbies)        # []  -> proves each person has a separate list

# Expected Output:
# Point(x=1, y=2)
# True
# Hi, I'm Alice and I'm 30 years old.
# Hi, I'm Bob and I'm 25 years old.
# ['reading']
# []
