"""
Exercise 21.5b: Adapter

Goal:
    The client calls predict().
    The library object only has infer().
    ModelAdapter stores an ExternalModel and translates predict() into infer().

    Do not edit Predictor, ExternalModel, or run_prediction().
    Write only ModelAdapter.

--------------------------------------------------------------------------------
The two sides do not match:

    client code          ModelAdapter            library
    model.predict(x)  -> self.model.infer(x) ->  returns 2.0 * x

Write it in two steps:

1. ModelAdapter.__init__(self, model)
    Save the library object so predict() can use it later.
        self.model = model
    model is an ExternalModel. Do not call infer() here.

2. ModelAdapter.predict(self, x)
    Call infer() on the object you stored, and return that number.
        return self.model.infer(x)
    Do not write 2.0 * x here. That formula already lives in ExternalModel.
    The adapter only forwards the call.

Check:
    ExternalModel().infer(3.0) is 6.0.
    run_prediction(...) calls predict(3.0), so the program should print 6.0.

How to run:
    python main.py
"""


class Predictor:
    def predict(self, x: float) -> float:
        raise NotImplementedError


class ExternalModel:
    """A stand-in for a library. It does not have predict()."""

    def infer(self, x: float) -> float:
        return 2.0 * x


class ModelAdapter(Predictor):
    def __init__(self, model: ExternalModel) -> None:
        # TODO: store the library object: self.model = model
        pass

    def predict(self, x: float) -> float:
        # TODO: return self.model.infer(x)
        pass


def run_prediction(model: Predictor, x: float) -> float:
    """Client code. It only knows about predict()."""
    return model.predict(x)


# ------------------------------- DO NOT EDIT -------------------------------- #

if __name__ == "__main__":
    print(run_prediction(ModelAdapter(ExternalModel()), 3.0))


# Expected Output:
# 6.0
