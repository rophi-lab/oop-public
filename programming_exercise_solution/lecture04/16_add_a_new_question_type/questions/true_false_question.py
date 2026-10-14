from questions.question import Question


class TrueFalseQuestion(Question):
    def __init__(self, title, prompt, points, correct_answer):
        super().__init__(title, prompt, points)
        self.correct_answer = correct_answer

    def display(self):
        print(f"{self.title}: {self.prompt}")
        print("Type True or False.")
        print()

    def check_answer(self, user_answer):
        user_answer = user_answer.lower()

        if user_answer == "true":
            user_value = True
        elif user_answer == "false":
            user_value = False
        else:
            return 0, "Invalid input. Please type True or False."

        if user_value == self.correct_answer:
            return self.points, "Correct!"

        return 0, f"Incorrect. The correct answer was {self.correct_answer}."
