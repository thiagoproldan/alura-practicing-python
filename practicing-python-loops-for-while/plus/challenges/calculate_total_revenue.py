"""
João received a list of values representing the revenues of his clothing store.
He wants to calculate the total sum of these revenues to understand the weekly financial performance.

values = [10, 20, 30, 40, 50]

Expected output:
The total sum of revenues is: 150

Create a program to help João calculate the total amount.
"""

values = [10, 20, 30, 40, 50]

total = 0
for value in values:
    total += value

print(f"The total sum of revenues is: {total}")