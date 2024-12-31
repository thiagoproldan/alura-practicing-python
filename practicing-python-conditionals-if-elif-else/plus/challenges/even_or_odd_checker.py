"""
Lucas is developing a game and needs a feature to check if a number is even or odd.
This check will be used to define different actions within the game. Write a program that takes an integer as input and displays a message indicating whether it is even or odd.

Expected output:
Enter an integer: 20
The number 20 is even.
"""

number = int(input("Enter an integer: "))

if number % 2 == 0:  # Checks if the number is even by verifying if the remainder of division by 2 is zero
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")