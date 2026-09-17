"""
Exercise 09: Book Class

Goal:
    Build a Book class and give it several SPECIAL (dunder) methods so that
    Python's built-in syntax works naturally on your objects.

Why this exercise?
    A class is more useful when it behaves like a built-in type. Instead of
    calling custom methods, you teach Python how print(), len(), and sorting
    should treat your object by implementing "dunder" (double-underscore)
    methods. Then `print(book)`, `len(book)`, and `books.sort()` all just work.

Special methods you will implement:
    - __init__(self, ...) -> the constructor; store the object's data.
    - __str__(self)       -> what print(book) shows (a readable string).
    - __len__(self)       -> what len(book) returns (here: the page count).
    - __lt__(self, other) -> the "less than" rule used when sorting a list.

How sorting uses __lt__:
    books.sort() repeatedly asks "is this book < that book?". Because __lt__
    compares by number of pages, the list ends up ordered from fewest to most
    pages.

TODO:
    1. Store title, author, and pages in __init__.
    2. Implement __str__, __len__, and __lt__ as described above.
    3. Match the Expected Output shown at the bottom of the file.
"""


class Book:
    def __init__(self, title, author, pages):
        # TODO: store title, author, and pages
        pass

    def __str__(self):
        # TODO: return a readable string
        pass

    def __len__(self):
        # TODO: return the number of pages
        pass

    def __lt__(self, other):
        # TODO: compare books by number of pages
        pass

book1 = Book("Python Basics", "Alice Kim", 120)
book2 = Book("OOP in Practice", "Chris Park", 200)
book3 = Book("Advanced Python", "Bob Lee", 300)

books = [book3, book1, book2]

print(book1)
print(len(book1))
books.sort()

for book in books:
    print(book)
    
# Expected Output:
# Python Basics by Alice Kim
# 120
# Python Basics by Alice Kim
# OOP in Practice by Chris Park
# Advanced Python by Bob Lee
