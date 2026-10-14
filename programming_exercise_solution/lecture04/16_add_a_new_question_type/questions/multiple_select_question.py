from questions.question import Question


class MultipleSelectQuestion(Question):
    def __init__(self, title, prompt, points, choices, correct_choices):
        super().__init__(title, prompt, points)
        self.choices = choices
        self.correct_choices = correct_choices

    def display(self):
        print(f"{self.title}: {self.prompt}")

        for i, choice in enumerate(self.choices):
            print(f"{i + 1}. {choice}")

        print("Select all correct answers.")
        print()

    def check_answer(self, user_answer):
        try:
            selected = [int(part.strip()) for part in user_answer.split(",") if part.strip()]
        except ValueError:
            return 0, "Invalid input. Please enter numbers separated by commas."

        if set(selected) == set(self.correct_choices):
            return self.points, "Correct!"

        return 0, f"Incorrect. The correct answers were {self.correct_choices}."
