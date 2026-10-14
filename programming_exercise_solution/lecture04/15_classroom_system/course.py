class Course:
    def __init__(self, title, instructor):
        self.title = title
        self.instructor = instructor
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def class_average(self):
        if not self.students:
            return 0
        return sum(student.average() for student in self.students) / len(self.students)

    def __len__(self):
        return len(self.students)

    def __iter__(self):
        return iter(self.students)

    def __str__(self):
        return f"{self.title} taught by {self.instructor.name}"