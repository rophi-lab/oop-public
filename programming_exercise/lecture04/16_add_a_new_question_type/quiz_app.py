"""
Exercise 16: Add a New Question Type

Goal:
    A quiz engine already runs multiple kinds of questions. Your job is to add
    one more type, MultipleSelectQuestion, by completing the class in
    questions/multiple_select_question.py.

Why this exercise?
    This is the payoff of INHERITANCE and POLYMORPHISM. The base class Question
    defines a shared workflow in ask() (display -> read input -> check ->
    score). Each question type only overrides the parts that differ (display
    and check_answer). Because the Quiz engine only relies on the shared
    interface, you can add a brand new question type WITHOUT touching the
    engine at all.

How the files fit together:
    - quiz_app.py                         -> this file; builds and runs a quiz.
    - engine/quiz.py                      -> loops over questions, sums scores.
    - questions/question.py               -> the base class (ask/display/check).
    - questions/*_question.py             -> the concrete question types.
    - questions/multiple_select_question.py -> YOU complete this one.

What "multiple select" means:
    The user may pick SEVERAL correct choices, entered like "1, 2, 4". You must
    parse that into [1, 2, 4] and award full points only if it matches the set
    of correct choices exactly. Order does not matter: "4, 1, 2" is the same
    as "1, 2, 4".

TODO:
    1. Open questions/multiple_select_question.py.
    2. Implement __init__ (super + store choices/correct_choices), display, and
       check_answer as described by its TODO comments.
    3. Run this file and answer Question 4 to test your new type.
"""

from engine.quiz import Quiz
from questions import (
    MultipleChoiceQuestion,
    NumericQuestion,
    TrueFalseQuestion,
    MultipleSelectQuestion
)


def main():
    quiz = Quiz("Basic Python OOP Quiz")

    quiz.add_question(
        MultipleChoiceQuestion(
            title="Question 1",
            prompt="Which keyword is used to define a function in Python?",
            points=2,
            choices=["class", "def", "return", "import"],
            correct_choice=2
        )
    )

    quiz.add_question(
        NumericQuestion(
            title="Question 2",
            prompt="What is the value of pi approximately?",
            points=2,
            correct_value=3.14,
            tolerance=0.01
        )
    )

    quiz.add_question(
        TrueFalseQuestion(
            title="Question 3",
            prompt="Python supports object-oriented programming.",
            points=2,
            correct_answer=True
        )
    )

    quiz.add_question(
        MultipleSelectQuestion(
            title="Question 4",
            prompt="Which of the following are Python collection types?",
            points=2,
            choices=["list", "tuple", "set", "dictionary"],
            correct_choices=[1, 2, 3, 4]
        )
    )

    quiz.run()

if __name__ == "__main__":
    main()