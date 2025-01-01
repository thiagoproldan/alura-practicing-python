"""
Ana is implementing a book filtering system for Buscante.
The functionality should iterate through a list of books and display the name of each book available in stock.
However, if the book is out of stock, it should be skipped during the iteration.

books = [
    {"name": "1984", "stock": 5},
    {"name": "Dom Casmurro", "stock": 0},
    {"name": "The Little Prince", "stock": 3},
    {"name": "The Hobbit", "stock": 0},
    {"name": "Pride and Prejudice", "stock": 2}
]

Create a program to help Ana display only the books that are available in stock, in the format: "Available book: ".

Expected output:
Available book: 1984
Available book: The Little Prince
Available book: Pride and Prejudice
"""

books = [
    {"name": "1984", "stock": 5},
    {"name": "Dom Casmurro", "stock": 0},
    {"name": "The Little Prince", "stock": 3},
    {"name": "The Hobbit", "stock": 0},
    {"name": "Pride and Prejudice", "stock": 2}
]

for book in books:
    if book["stock"] == 0:
        continue
    print(f"Available book: {book['name']}")