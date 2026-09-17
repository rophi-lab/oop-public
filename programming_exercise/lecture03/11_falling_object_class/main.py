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
        # TODO: store name, height, and velocity
        # height: initial height in meters
        # velocity: initial downward velocity in m/s
        pass

    def position_after(self, time):
        # TODO: return the height after time seconds
        # Use: new_height = height - velocity * time - 0.5 * 9.8 * time ** 2
        # The height should not go below 0
        pass
    
    def velocity_after(self, time):
        # TODO: return the downward velocity after time seconds
        # Use: new_velocity = velocity + 9.8 * time
        pass

    def __str__(self):
        # TODO: return a readable string
        pass

    def __bool__(self):
        # TODO: return False if the object already starts on the ground
        # Otherwise return True
        pass

    def __lt__(self, other):
        # TODO: compare objects by initial height
        pass

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
