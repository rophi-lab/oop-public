class Library:
    def __init__(self, name):
        self._name = name
        self._books = {}
        self._members = {}

    def add_book(self, book):
        # TODO: add the book to the books dictionary using its ISBN
        pass

    def register_member(self, member):
        # TODO: add the member to the members dictionary using member ID
        pass

    def borrow_book(self, member_id, isbn):
        # TODO: let a registered member borrow an available book
        pass

    def return_book(self, member_id, isbn):
        # TODO: let a member return a borrowed book
        pass
