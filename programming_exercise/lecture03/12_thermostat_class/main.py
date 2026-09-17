"""
Exercise 12: Thermostat Class

Goal:
    Build a Thermostat whose temperature can only ever be a valid value (10 to
    30). Use a PROPERTY so that validation happens automatically every time the
    temperature is set.

Why this exercise?
    This introduces `@property` and `@<name>.setter`, Python's way of running
    code when an attribute is read or assigned. Instead of exposing a raw
    attribute that anyone could set to a nonsense value, a property lets you
    guard it: `room.temperature = 100` should raise an error, not silently
    store an impossible temperature. This is called ENCAPSULATION.

Key ideas:
    - Store the real value in a "private" attribute like self._temperature.
    - @property temperature      -> the getter; returns self._temperature.
    - @temperature.setter        -> validates, then stores the value.
    - increase()/decrease() should go THROUGH the property (self.temperature =
      ...) so the same validation still runs.
    - Invalid values must raise ValueError("Invalid temperature").

TODO:
    1. Implement the getter and setter with the 10-30 validation.
    2. Implement increase(), decrease(), and status().
    3. Match the Expected Output shown at the bottom of the file.
"""


class Thermostat:
    def __init__(self, temperature=20):
        # TODO: store temperature using the setter
        pass

    @property
    def temperature(self):
        # TODO: return the internal temperature
        pass

    @temperature.setter
    def temperature(self, value):
        # TODO: temperature must be between 10 and 30
        # If value is invalid, raise ValueError("Invalid temperature")
        pass

    def increase(self, amount):
        # TODO: increase temperature by amount
        # Use the property so that validation is still applied
        pass

    def decrease(self, amount):
        # TODO: decrease temperature by amount
        # Use the property so that validation is still applied
        pass

    def status(self):
        # TODO: return "Cold", "Comfortable", or "Hot"
        # below 18: "Cold"
        # 18 to 25: "Comfortable"
        # above 25: "Hot"
        pass

room = Thermostat(22)

print(room.temperature)
print(room.status())

room.increase(5)
print(room.temperature)
print(room.status())
room.decrease(10)
print(room.temperature)
print(room.status())

try:
    room.temperature = 100
except ValueError as e:
    print(e)

# Expected Output:
# 22
# Comfortable
# 27
# Hot
# 17
# Cold
# Invalid temperature
