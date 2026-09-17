"""
Exercise 08: Create Your Own Python Modules

Goal:
    Split reusable functions into separate files (MODULES) and use them from
    this main program by importing them.

Why this exercise?
    As programs grow, keeping every function in one file becomes messy. Python
    lets you organize related functions into their own `.py` files and reuse
    them wherever you need. A file named `math_utils.py` becomes a module you
    can `import math_utils` and then call as `math_utils.add(1, 2)`. This is
    exactly how the standard library (math, random, datetime, ...) is built.

How the files fit together:
    - main.py        -> this file; it imports the modules and calls them.
    - math_utils.py  -> add(), multiply(), distance()   (you implement these)
    - robot_utils.py -> print_robot_status(), is_battery_low()  (you implement)

Reminder about return vs print:
    Functions that RETURN a value are wrapped in print(...) here so you can
    see the result. print_robot_status PRINTS by itself, so it is called
    without an outer print -- otherwise you would also see None. Read each
    function's docstring to see whether it should return or print.

TODO:
    1. Open math_utils.py and implement add, multiply, and distance.
    2. Open robot_utils.py and implement print_robot_status and is_battery_low.
    3. Do NOT change this file; just make the imported functions work.
"""

import math_utils
import robot_utils

print(math_utils.add(1, 2))
print(math_utils.multiply(1, 2))
print(math_utils.distance(1, 2, 3, 4))

# print_robot_status prints by itself -- do not wrap it in print(...),
# or you would also see None (the function's return value).
robot_utils.print_robot_status("Robot1", 50)
print(robot_utils.is_battery_low(50))
