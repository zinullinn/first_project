"""Using sorted and lambda for custom ordering."""

books = [("Python Basics", 320), ("Clean Code", 464), ("Algorithms", 250)]

# Here is sorted with lambda to order books by page count.
books_by_pages = sorted(books, key=lambda book: book[1])

print(books_by_pages)
