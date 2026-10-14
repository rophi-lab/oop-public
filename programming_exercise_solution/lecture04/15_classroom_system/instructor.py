class Instructor:
    def __init__(self, name):
        self.name = name
    
    def give_score(self, student, score):
        student.add_score(score)