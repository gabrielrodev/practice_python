# Aggregation = Represents a relationship were one object (the whole)
#               Contains references to one or more Independent object (the parts)

class Library: # cotainer of references to one or more independent objects, the whole.(independent)
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [f"{book.tittle} by {book.author}"for book in self.books]
class Book: # The parts (independent)
    def __init__(self,tittle, author):
        self.tittle = tittle
        self.author = author

library = Library("New York Public Library")

book1 = Book("The judge list.","John Grisham")
book2 = Book("Ventajas de ser invisible","Stephen Chbosky")
book3 = Book("Percy Jackson ", "Rick Riordan")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

for book in library.list_books():
    print(book)
