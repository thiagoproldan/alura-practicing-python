"""
You are developing an inventory control system for Buscante.
One of the requirements is to check the number of copies of a book in stock and continue selling until the stock is depleted.
Whenever a sale is made, the system must inform the user and update the available quantity.

Create a program that simulates book sales with an initial stock of 5 copies.
The program should display the message "Sale completed! Remaining stock: <quantity>" for each sale and, at the end, display the message "Stock depleted!".

Expected output:
Sale completed! Remaining stock: 5
Sale completed! Remaining stock: 4
Sale completed! Remaining stock: 3
Sale completed! Remaining stock: 2
Sale completed! Remaining stock: 1
Stock depleted!
"""

book_stock = 5

while book_stock > 0:
    print(f"Sale completed! Remaining stock: {book_stock}")
    book_stock -= 1

print("Stock depleted!")