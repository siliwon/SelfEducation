# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


class Book:
    def __init__(self, title):
        self.title = title


b1 = Book("Brave New World")
b2 = Book("War and Peace")

print(b1)
print(b1.title)
