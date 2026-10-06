"""
Exercise 11: Falling Object Class

Goal:
    Model a falling object under gravity. The class stores an initial height
    and velocity and can compute its height and speed after some time.

Why this exercise?
    Here a class holds STATE (height, velocity) and provides methods that do
    real physics calculations from that state. It combines object-oriented
    design with a simple physics formula, and reuses the special methods from
    earlier exercises (__str__, __bool__, __lt__).

The physics (already given in the TODO comments):
    - position: new_height = height - velocity * time - 0.5 * 9.8 * time ** 2
    - velocity: new_velocity = velocity + 9.8 * time
    - Height should never drop below 0 (it has hit the ground).

Special methods you will implement:
    - __init__  -> store name, height, and velocity (velocity defaults to 0).
    - __str__   -> a readable string, e.g. "Ball starts at 20 m".
    - __bool__  -> False if it already starts on the ground (height 0).
    - __lt__    -> compare objects by initial height (used for sorting).

TODO:
    1. Implement position_after() and velocity_after() using the formulas.
    2. Implement __str__, __bool__, and __lt__.
    3. Match the Expected Output shown at the bottom of the file.
"""


class FallingObject:
    def __init__(self, name, height, velocity=0):
        self.name = name
        self.height = height
        self.velocity = velocity

    def position_after(self, time):
        new_height = self.height - self.velocity * time - 0.5 * 9.8 * time ** 2
        return max(new_height, 0)
    
    def velocity_after(self, time):
        return self.velocity + 9.8 * time

    def __str__(self):
        return f"{self.name} starts at {self.height} m"

    def __bool__(self):
        return self.height != 0

    def __lt__(self, other):
        return self.height < other.height

def print_motion_info(obj, time):
    print(obj)

    if obj:
        print("Height after", time, "seconds:", obj.position_after(time), "m")
        print("Velocity after", time, "seconds:", obj.velocity_after(time), "m/s")
    else:
        print("This object is already on the ground.")


ball = FallingObject("Ball", 20)
stone = FallingObject("Stone", 50)
box = FallingObject("Box", 0)

print_motion_info(ball, 2)
print_motion_info(box, 2)

objects = [stone, box, ball]
objects.sort()

print("Sorted by initial height:")
for obj in objects:
    print(obj)
    
# Expected Output:

# Ball starts at 20 m
# Height after 2 seconds: 0.3999999999999986 m
# Velocity after 2 seconds: 19.6 m/s
# Box starts at 0 m
# This object is already on the ground.
# Sorted by initial height:
# Box starts at 0 m
# Ball starts at 20 m
# Stone starts at 50 m
