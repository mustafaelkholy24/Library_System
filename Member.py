class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.books = []

    def borrow_book(self, book):
        self.books.append(book)

    def return_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def member_info(self):
        print(f"- [{self.member_id}] {self.name} is borrowed {len(self.books)} books")
        if self.books:
            print("     Borrowed books:")
            for book in self.books:
                print(f"        - {book}")
        else:
            print("     - Member has no books")