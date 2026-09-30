"""
Exercise 15: Classroom System

Goal:
    Build a small classroom made of three cooperating classes: Student,
    Instructor, and Course. Together they can enroll students, record scores,
    and report averages.

Why this exercise?
    This is another COMPOSITION exercise: a Course contains Students and an
    Instructor, and objects interact (an Instructor gives a score to a
    Student). You also make Course behave like a container by implementing
    __len__ (number of students) and __iter__ (loop over students), so
    `len(course)` and `for student in course:` work naturally.

How the files fit together:
    - main.py       -> this driver; builds the classroom and prints results.
    - student.py    -> stores a name and a list of scores; computes average().
    - instructor.py -> give_score(student, score): calls the student's method.
    - course.py     -> holds the instructor and a list of students.

The methods you implement:
    - Student:    __init__, add_score (validate 0-100), average, __str__.
    - Instructor: __init__, give_score (delegates to the Student object).
    - Course:     __init__, add_student, class_average, __len__, __iter__, __str__.

Attribute names (public, not _private):
    Student.name, Student.scores, Instructor.name, Course.title,
    Course.instructor, Course.students. Course.__str__ should read
    self.instructor.name.

Note on interaction:
    Instructor.give_score should NOT store scores itself; it should call
    student.add_score(...). That is the point of objects talking to each other.

TODO:
    1. Implement student.py, instructor.py, and course.py.
    2. Handle empty cases (average of no scores / no students is 0).
    3. Match the Expected Output shown at the bottom of this file.
"""

from instructor import Instructor
from course import Course
from student import Student

teacher = Instructor("Dr. Kim")
course = Course("Python OOP", teacher)

alice = Student("Alice")
bob = Student("Bob")
charlie = Student("Charlie")

course.add_student(alice)
course.add_student(bob)
course.add_student(charlie)

teacher.give_score(alice, 90)
teacher.give_score(alice, 80)
teacher.give_score(bob, 70)
teacher.give_score(bob, 75)
teacher.give_score(charlie, 100)
teacher.give_score(charlie, 95)

print(course)
print("Number of students:", len(course))

print("Roster:")
for student in course:
    print(student)

print("Class average:", round(course.class_average(), 1))

print("Empty average:", Student("Dana").average())

try:
    teacher.give_score(alice, 150)
except ValueError as error:
    print(error)

# Expected Output:

# Python OOP taught by Dr. Kim
# Number of students: 3
# Roster:
# Alice (average: 85.0)
# Bob (average: 72.5)
# Charlie (average: 97.5)
# Class average: 85.0
# Empty average: 0
# Invalid score
