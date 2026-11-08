class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_borrowed = False

    def borrow_book(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"[{self.book_id}] {self.title} - {self.author} ({status})"