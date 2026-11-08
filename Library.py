class Library:
    def __init__(self):
        self.__books = []
        self.__members = []

    def add_book(self, book):
        self.__books.append(book)
        # print("Successfully Added Book.")

    def add_member(self, member):
        self.__members.append(member)
        # print("Successfully Added Member.")

    def find_book(self, book_id):
        for book in self.__books:
            if book_id == book.book_id:
                return book
        return None

    def find_member(self, member_id):
        for member in self.__members:
            if member_id == member.member_id:
                return member
        return None

    def borrow_book(self, book_id,member_id):
        book = self.find_book(book_id)
        member = self.find_member(member_id)

        if not member:
            print("Member not found.")
            return

        if not book:
            print("Book not found.")
            return

        if book.is_borrowed:
            print("Book already borrowed.")

        else:
            book.borrow_book()
            member.borrow_book(book)
            print("Successfully Borrowed Book.")

    def return_book(self, book_id, member_id):
        book = self.find_book(book_id)
        member = self.find_member(member_id)
        if member and book:
            if book in member.books:
                book.return_book()
                member.return_book(book)
                print("Successfully Returned Book.")
            else:
                print("Book not found with this member.")
        else:
            print("Error in Member or Book Data.")


    def display_all_books(self):
        print("Books Data: ")
        if not self.__books:
            print("No books found.")
            return

        for book in self.__books:
            print(f"    - {book}")

    def display_all_members(self):
        print("Members Data: ")
        if not self.__members:
            print("No members found.")
            return

        for member in self.__members:
            member.member_info()