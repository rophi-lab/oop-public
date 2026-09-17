"""
Exercise 10: Rectangle Class

Goal:
    Build a Rectangle class with real behavior (area, perimeter) and several
    special methods so it works with Python's built-in syntax.

Why this exercise?
    This builds on the Book exercise by adding two new dunder methods: __bool__
    (truthiness) and more practice with sorting. It shows how one object can
    respond correctly to many built-in operations at once, which is what makes
    custom classes feel like a natural part of the language.

Special methods you will implement:
    - __init__  -> store width and height.
    - __str__   -> a readable string, e.g. "Rectangle(width=3, height=4)".
    - __len__   -> the area as an integer (used by len(shape)).
    - __bool__  -> False when the area is 0, otherwise True.
    - __lt__    -> compare rectangles by area (used for sorting).

Where __bool__ matters:
    Look at print_shape_info(): `if shape:` calls your __bool__. A rectangle
    with zero area (like width 0) should be treated as "empty" / falsy.

TODO:
    1. Implement area() and perimeter().
    2. Implement __str__, __len__, __bool__, and __lt__.
    3. Match the Expected Output shown at the bottom of the file.
"""


class Rectangle:
    def __init__(self, width, height):
        # TODO: store width and height
        pass

    def area(self):
        # TODO: return the area
        pass

    def perimeter(self):
        # TODO: return the perimeter
        pass
    
    def __str__(self):
        # TODO: return a readable string
        pass

    def __len__(self):
        # TODO: return the area as an integer
        pass

    def __bool__(self):
        # TODO: return False if area is 0, otherwise True
        pass

    def __lt__(self, other):
        # TODO: compare rectangles by area
        pass

def print_shape_info(shape):
    print(shape)
    print("Area:", len(shape))
    if shape:
        print("This is a valid shape.")
    else:
        print("This is an empty shape.")


r1 = Rectangle(3, 4)
r2 = Rectangle(5, 2)
r3 = Rectangle(0, 10)

print_shape_info(r1)
print_shape_info(r3)

rectangles = [r1, r2, r3]
rectangles.sort()

print("Sorted rectangles:")
for r in rectangles:
    print(r)

# Expected Output:
# Rectangle(width=3, height=4)
# Area: 12
# This is a valid shape.
# Rectangle(width=0, height=10)
# Area: 0
# This is an empty shape.
# Sorted rectangles:
# Rectangle(width=0, height=10)
# Rectangle(width=5, height=2)
# Rectangle(width=3, height=4)
