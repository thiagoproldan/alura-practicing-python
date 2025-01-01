"""
Aline is implementing a feature that displays personalized messages to customers during a special promotion for her new bookstore.
The system should display a personalized countdown message for each number from 10 to 1, and at the end, display the message: "Enjoy the promotion now!".

Create a program using a for loop to display the following messages:

    For even numbers, display: "Only <number> seconds left - Don't miss this opportunity!".
    For odd numbers, display: "The countdown continues: <number> seconds remaining.".
    At the end of the countdown, display the message: "Enjoy the promotion now!".

Expected output:
Only 10 seconds left - Don't miss this opportunity!
The countdown continues: 9 seconds remaining.
Only 8 seconds left - Don't miss this opportunity!
The countdown continues: 7 seconds remaining.
Only 6 seconds left - Don't miss this opportunity!
The countdown continues: 5 seconds remaining.
Only 4 seconds left - Don't miss this opportunity!
The countdown continues: 3 seconds remaining.
Only 2 seconds left - Don't miss this opportunity!
The countdown continues: 1 seconds remaining.
Enjoy the promotion now!
"""

for seconds in range(10, 0, -1): # Range(10, 0, -1) generates numbers from 10 to 1 in descending order. The first parameter is the start, the second is the end, and the third is the step.
    if seconds % 2 == 0: # The % operator returns the remainder of the division between two numbers. If the remainder is 0, the number is even.
        print(f"Only {seconds} seconds left - Don't miss this opportunity!")
    else:
        print(f"The countdown continues: {seconds} seconds remaining.")

print("Enjoy the promotion now!")