"""
Exercise 21.5d: Decorator

Goal:
    LoggingPredictor wraps another predictor and adds a print.
    The wrapped object still does the real work.
    Do not edit Predictor or DoublePredictor.

--------------------------------------------------------------------------------
DoublePredictor.predict(x) already returns 2.0 * x.
LoggingPredictor does not repeat that formula. It holds a predictor and
calls that predictor's predict().

1. LoggingPredictor.__init__(self, wrapped)
    Save the object you are wrapping:
        self.wrapped = wrapped
    wrapped is a Predictor, for example a DoublePredictor.
    Do not call predict() here.

2. LoggingPredictor.predict(self, x)
    Do these three lines, in this order:
        a. result = self.wrapped.predict(x)
        b. print this exact text, with the input and the result:
               predict(<x>) = <result>
           An f-string does that:
               print(f"predict({x}) = {result}")
        c. return result
           Return the same number you printed. Do not compute it again.

Check with the demo:
    LoggingPredictor(DoublePredictor()).predict(3.0)
    DoublePredictor returns 6.0, so the program prints

        predict(3.0) = 6.0
        6.0

    The second line is the print() in the "DO NOT EDIT" section.
    Your print() is the first line.

How to run:
    python main.py
"""


class Predictor:
    def predict(self, x: float) -> float:
        raise NotImplementedError


class DoublePredictor(Predictor):
    def predict(self, x: float) -> float:
        return 2.0 * x


class LoggingPredictor(Predictor):
    def __init__(self, wrapped: Predictor) -> None:
        # TODO: store the wrapped predictor: self.wrapped = wrapped
        pass

    def predict(self, x: float) -> float:
        # TODO: result = self.wrapped.predict(x)
        # TODO: print(f"predict({x}) = {result}")
        # TODO: return result
        pass


# ------------------------------- DO NOT EDIT -------------------------------- #

if __name__ == "__main__":
    print(LoggingPredictor(DoublePredictor()).predict(3.0))


# Expected Output:
# predict(3.0) = 6.0
# 6.0
