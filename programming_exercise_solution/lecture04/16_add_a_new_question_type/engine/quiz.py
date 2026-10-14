class Quiz:
    def __init__(self, title):
        self.title = title
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def run(self):
        print("=" * 50)
        print(self.title)
        print("=" * 50)
        print()

        total_score = 0
        total_points = 0

        for question in self.questions:
            score = question.ask()

            total_score += score
            total_points += question.points

        print("=" * 50)
        print("Quiz finished!")
        print(f"Final score: {total_score} / {total_points}")
        print("=" * 50)
