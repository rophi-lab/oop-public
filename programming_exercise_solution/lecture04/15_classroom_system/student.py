class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score):
        if score < 0 or score > 100:
            raise ValueError("Invalid score")
        self.scores.append(score)

    def average(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

    def __str__(self):
        return f"{self.name} (average: {self.average()})"