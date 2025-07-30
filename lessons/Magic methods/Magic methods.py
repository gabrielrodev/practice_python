# Magic methods = Dunder methods (they have double underscore) __init__,__str__,__eq__
#                 They are automatically called by many of python's built-in operations.
#                 They allow developers to define or customize the behavior of objects

# customize the behavior of objects
class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self): # works for strings
        return f"{self.title} by {self.author}"

    def __eq__(self, other): # works for equal sings
        return self.title == other.title and self.author == other.author

    def __lt__(self, other): #less than
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return f"Total pages: {self.num_pages + other.num_pages}"

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == 'title':
            return self.title
        elif key == 'author':
            return self.author
        elif key == 'num_pages':
            return self.num_pages
        else:
            return f"Key {key} is not valid"

book1 = Book("Python", "Chris", 302)
book2 = Book("As a Man Thinketh", "James",134)
book3 = Book("king julian", "Elliot Owen", 463)

#print(book3)
#print(book1 == book3) # to say yes it has to have all of its varibles equal to  each other
#print(book2 < book3)
#print(book1 > book2)
#print(book1 + book2)
#print("Chris" in book1)
#print(book3[''])
