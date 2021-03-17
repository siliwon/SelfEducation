# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    __booklist = None

    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    @staticmethod
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance

    def setTitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title, book_type):
        self.title = title
        if not book_type in Book.BOOK_TYPES:
            raise ValueError(f"{book_type} is not a valid book type")
        else:
            self.booktype = book_type


print("Book types: ", Book.getbooktypes())

b1 = Book("Title 1", "HARDCOVER")
b2 = Book("Title 2", "PAPERBACK")

thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)
