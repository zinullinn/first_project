"""A class definition and object creation example."""


class Book:
    """Represent a book in a small library."""

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def description(self):
        return f"{self.title} by {self.author}"


# Here is an object created from the Book class.
favorite_book = Book("The Alchemist", "Paulo Coelho")
print(favorite_book.description())
