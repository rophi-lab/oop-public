from questions.question import Question


class MultipleChoiceQuestion(Question):
    def __init__(self, title, prompt, points, choices, correct_choice):
        super().__init__(title, prompt, points)
        self.choices = choices
        self.correct_choice = correct_choice

    def display(self):
        print(f"{self.title}: {self.prompt}")

        for i, choice in enumerate(self.choices):
            print(f"{i + 1}. {choice}")

        print()

    def check_answer(self, user_answer):
        try:
            user_choice = int(user_answer)
        except ValueError:
            return 0, "Invalid input. Please enter a number."

        if user_choice == self.correct_choice:
            return self.points, "Correct!"
        else:
            return 0, f"Incorrect. The correct answer was {self.correct_choice}."
