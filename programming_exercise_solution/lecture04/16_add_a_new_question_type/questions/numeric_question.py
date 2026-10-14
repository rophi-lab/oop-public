from questions.question import Question


class NumericQuestion(Question):
    def __init__(self, title, prompt, points, correct_value, tolerance):
        super().__init__(title, prompt, points)
        self.correct_value = correct_value
        self.tolerance = tolerance

    def check_answer(self, user_answer):
        try:
            user_value = float(user_answer)
        except ValueError:
            return 0, "Invalid input. Please enter a number."

        error = abs(user_value - self.correct_value)

        if error <= self.tolerance:
            return self.points, "Correct!"

        return 0, f"Incorrect. The correct answer was about {self.correct_value}."
