"""
José is developing a feature for the Buscante system to stop the search as soon as a specific book is found.
The list of books already registered in the system is as follows:

books = ["1984", "Dom Casmurro", "The Little Prince", "The Hobbit", "Pride and Prejudice"]

Help José create a program that iterates through the list and displays the message "Book found: <book name>" as soon as the book "The Hobbit" is found.
After finding the book, the program must stop the search immediately without checking the remaining books.

Expected output:
Book found: The Hobbit
"""

books = ["1984", "Dom Casmurro", "The Little Prince", "The Hobbit", "Pride and Prejudice"]

search_book = "The Hobbit"

for book in books:
    if book == search_book:
        print(f"Book found: {book}")
        break