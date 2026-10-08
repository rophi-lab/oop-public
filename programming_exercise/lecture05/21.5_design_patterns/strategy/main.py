"""
Exercise 21.5a: Strategy

Goal:
    ScoreProcessor.process() always calls strategy.normalize().
    Change the algorithm by swapping the strategy object.
    Do not edit ScoreProcessor.

Write only the three normalize() methods. Replace each pass.
Each method receives values, a list of floats, and returns a new list.
Do not change the list that was passed in.

--------------------------------------------------------------------------------
1. IdentityNormalizer.normalize
    Return a copy of values.
    Use values.copy().

    Check: [2.0, 4.0] stays [2.0, 4.0].

2. MinMaxNormalizer.normalize
    Rescale every value into the range 0.0 .. 1.0.

    Follow these steps in order:
        a. If values is empty, return [].
        b. low = min(values)
           high = max(values)
        c. If low == high, every value is the same.
           Return a list of 0.0 with the same length as values.
           You can build it with [0.0 for value in values].
        d. Otherwise return a new list. For each value use
               (value - low) / (high - low)

    Check by hand for [-2.0, 0.0, 2.0]:
        low = -2.0, high = 2.0
        (-2.0 - -2.0) / 4.0 = 0.0
        ( 0.0 - -2.0) / 4.0 = 0.5
        ( 2.0 - -2.0) / 4.0 = 1.0
        so the result is [0.0, 0.5, 1.0].

    Also check [2.0, 4.0] -> [0.0, 1.0].

3. MeanCenterNormalizer.normalize
    Subtract the mean from every value.

    Follow these steps in order:
        a. If values is empty, return [].
        b. mean = sum(values) / len(values)
        c. Return a new list. For each value use value - mean.

    A constant list becomes zeros because every value equals the mean.
    Check: [2.0, 4.0, 6.0] has mean 4.0, so the result is [-2.0, 0.0, 2.0].
    Check: [5.0, 5.0] becomes [0.0, 0.0].

How to run:
    python main.py

The printed lists should match the Expected Output at the bottom of this file.
"""


class Normalizer:
    def normalize(self, values: list[float]) -> list[float]:
        raise NotImplementedError


class IdentityNormalizer(Normalizer):
    def normalize(self, values: list[float]) -> list[float]:
        # TODO: return values.copy().
        pass


class MinMaxNormalizer(Normalizer):
    def normalize(self, values: list[float]) -> list[float]:
        # TODO: if values is empty, return [].
        # TODO: low = min(values), high = max(values).
        # TODO: if low == high, return a list of 0.0 with the same length.
        # TODO: otherwise return [(value - low) / (high - low) for each value].
        pass


class MeanCenterNormalizer(Normalizer):
    def normalize(self, values: list[float]) -> list[float]:
        # TODO: if values is empty, return [].
        # TODO: mean = sum(values) / len(values).
        # TODO: return [value - mean for each value].
        #       [2.0, 4.0, 6.0] -> [-2.0, 0.0, 2.0]
        pass


class ScoreProcessor:
    """Shared client. Do not change this class."""

    def __init__(self, strategy: Normalizer) -> None:
        self.strategy = strategy

    def process(self, values: list[float]) -> list[float]:
        return self.strategy.normalize(values)


# ------------------------------- DO NOT EDIT -------------------------------- #

if __name__ == "__main__":
    processor = ScoreProcessor(IdentityNormalizer())
    print(processor.process([2.0, 4.0]))

    processor.strategy = MinMaxNormalizer()
    print(processor.process([2.0, 4.0]))
    print(processor.process([-2.0, 0.0, 2.0]))

    processor.strategy = MeanCenterNormalizer()
    print(processor.process([2.0, 4.0, 6.0]))
    print(processor.process([5.0, 5.0]))
    print(processor.process([]))


# Expected Output:
# [2.0, 4.0]
# [0.0, 1.0]
# [0.0, 0.5, 1.0]
# [-2.0, 0.0, 2.0]
# [0.0, 0.0]
# []
