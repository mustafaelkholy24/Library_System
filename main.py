from data import books_data, members_data
from Books import Book
from Member import Member
from Library import Library

library = Library()

for book_id in books_data.keys():
    library.add_book(Book(books_data[book_id]['title'], books_data[book_id]['author'], book_id))

for member_id in members_data.keys():
    library.add_member(Member(members_data[member_id]['name'], member_id))

library.borrow_book("101", "M1")
library.borrow_book("102", "M1")
library.borrow_book("103", "M3")
library.borrow_book("104", "M5")

library.return_book("101", "M1")

library.display_all_members()
library.display_all_books()