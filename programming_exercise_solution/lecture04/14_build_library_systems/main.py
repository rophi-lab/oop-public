"""
Exercise 14: Build a Library System

Goal:
    Complete the Library class so that a library made of many cooperating
    objects (books and members) works correctly: books can be added, members
    registered, and books borrowed and returned.

Why this exercise?
    Real object-oriented programs are made of several classes that TALK to each
    other. Here a Library coordinates Book and Member objects. This teaches
    "composition": the Library does not do everything itself; it delegates to
    the books and members it holds. Notice you only edit library.py; the Book
    and Member classes are already finished for you to use.

How the files fit together:
    - main.py    -> this driver; creates objects and prints results.
    - book.py    -> a single book; knows if it is available and who has it.
    - member.py  -> a single member; tracks which books they borrowed.
    - library.py -> YOU implement this; it manages books and members by id.

The methods you implement (in library.py):
    - add_book(book)              -> store the book, keyed by its ISBN.
    - register_member(member)     -> store the member, keyed by member id.
    - borrow_book(member_id, isbn)-> if the member and book exist and the book
                                     is available, update both objects and
                                     return:
                                         {name} borrowed '{title}'.
                                     If the book is already out, return:
                                         '{title}' is not available.
    - return_book(member_id, isbn)-> reverse a borrow and return:
                                         {name} returned '{title}'.

Tip:
    Use the existing methods on Book (checkout/checkin/is_available) and Member
    (borrow/return_book) instead of touching their private attributes directly.

TODO:
    1. Open library.py and implement the four methods above.
    2. Use the books/members dictionaries keyed by isbn / member_id.
    3. Match the Expected Output shown at the bottom of this file.
    4. Do NOT change this file.
"""

from library import Library
from book import Book
from member import Member

library = Library("Central City Library")
library.add_book(Book("Clean Code", "978-0132350884"))
library.add_book(Book("Design Patterns", "978-0201633610"))

alice = Member("Alice Chen", "M001")
bob = Member("Bob Rivera", "M002")
library.register_member(alice)
library.register_member(bob)

print(library.borrow_book("M001", "978-0132350884")) 
print(alice) 
print(bob)
print("--------------------------------")
print(library.borrow_book("M002", "978-0132350884"))
print(alice)
print(bob)
print("--------------------------------")
print(library.return_book("M001", "978-0132350884"))
print(alice)
print(bob)
print("--------------------------------")
print(library.borrow_book("M002", "978-0132350884"))
print(alice)
print(bob)

# Expected Output:
# Alice Chen borrowed 'Clean Code'.
# Member('Alice Chen', borrowed=['Clean Code'])
# Member('Bob Rivera', borrowed=[])
# --------------------------------
# 'Clean Code' is not available.
# Member('Alice Chen', borrowed=['Clean Code'])
# Member('Bob Rivera', borrowed=[])
# --------------------------------
# Alice Chen returned 'Clean Code'.
# Member('Alice Chen', borrowed=[])
# Member('Bob Rivera', borrowed=[])
# --------------------------------
# Bob Rivera borrowed 'Clean Code'.
# Member('Alice Chen', borrowed=[])
# Member('Bob Rivera', borrowed=['Clean Code'])
