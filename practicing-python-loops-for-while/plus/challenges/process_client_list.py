"""
Ana is developing a program that needs to process a list of 5 client names to generate monthly reports.
For this, she needs to write a program that iterates through the list of names and displays each client.

clients = ["João", "Maria", "Carlos", "Ana", "Beatriz"]

Help Ana decide whether to use a `for` loop or a `while` loop.
Write the program using the loop you believe is most suitable for this task and explain why you chose that loop.
"""

clients = ["João", "Maria", "Carlos", "Ana", "Beatriz"]

for client in clients:
    print(f"Client: {client}")