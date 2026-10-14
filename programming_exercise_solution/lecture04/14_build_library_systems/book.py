class Book:
    def __init__(self, title, isbn):
        self._title = title
        self._isbn = isbn
        self._is_available = True
        self._borrowed_by = None

    def get_title(self):
        return self._title

    def get_isbn(self):
        return self._isbn

    def is_available(self):
        return self._is_available

    def get_borrowed_by(self):
        return self._borrowed_by

    def checkout(self, member):
        self._is_available = False
        self._borrowed_by = member

    def checkin(self):
        self._is_available = True
        self._borrowed_by = None

    def __repr__(self):
        status = "available" if self._is_available else "checked out"
        return f"Book({self._title!r}, {status})"
