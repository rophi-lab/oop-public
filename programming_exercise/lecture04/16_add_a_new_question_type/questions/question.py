class Question:
    def __init__(self, title, prompt, points):
        self.title = title
        self.prompt = prompt
        self.points = points

    def ask(self):
        """
        Common question workflow.

        1. Display the question
        2. Get user input
        3. Check the answer
        4. Print feedback
        5. Return the score
        """
        self.display()

        user_answer = input("Your answer: ")

        earned, feedback = self.check_answer(user_answer)

        # Common safety rule
        if earned < 0:
            earned = 0
        if earned > self.points:
            earned = self.points

        print(feedback)
        print(f"Score: {earned} / {self.points}")
        print()

        return earned

    def display(self):
        print(f"{self.title}: {self.prompt}")

    def check_answer(self, user_answer):
        """
        Child classes must override this method.
        """
        raise NotImplementedError("Child class must implement check_answer()")

