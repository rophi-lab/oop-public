class Member:
    def __init__(self, name, member_id):
        self._name = name
        self._member_id = member_id
        self._borrowed_books = []

    def get_name(self):
        return self._name

    def get_member_id(self):
        return self._member_id

    def get_borrowed_books(self):
        return list(self._borrowed_books)
    
    def borrow(self, book):
        self._borrowed_books.append(book)

    def return_book(self, book):
        self._borrowed_books.remove(book)
    
    def __repr__(self):
        titles = [book.get_title() for book in self._borrowed_books]
        return f"Member({self._name!r}, borrowed={titles})"
