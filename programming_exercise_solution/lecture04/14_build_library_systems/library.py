class Library:
    def __init__(self, name):
        self._name = name
        self._books = {}
        self._members = {}

    def add_book(self, book):
        self._books[book.get_isbn()] = book

    def register_member(self, member):
        self._members[member.get_member_id()] = member

    def borrow_book(self, member_id, isbn):
        member = self._members.get(member_id)
        book = self._books.get(isbn)

        if member is None:
            return "Member not found."
        if book is None:
            return "Book not found."
        if not book.is_available():
            return f"'{book.get_title()}' is not available."

        book.checkout(member)
        member.borrow(book)
        return f"{member.get_name()} borrowed '{book.get_title()}'."

    def return_book(self, member_id, isbn):
        member = self._members.get(member_id)
        book = self._books.get(isbn)

        if member is None:
            return "Member not found."
        if book is None:
            return "Book not found."
        if book.get_borrowed_by() is not member:
            return f"{member.get_name()} did not borrow '{book.get_title()}'."

        book.checkin()
        member.return_book(book)
        return f"{member.get_name()} returned '{book.get_title()}'."
