"""
Bruno manages a small store and wants to know which product performed best in sales last month.
He recorded the sales quantity of two products: apples and bananas.
Now, he needs to write a program to identify and display which of them had higher sales.
Create a program that receives the number of sales for the two products and displays a message indicating which one sold more.
If the quantities are equal, display a message saying there was a tie.

Expected output:
Enter the number of apples sold: 15
Enter the number of bananas sold: 3
Apples had higher sales.
"""

apples_sold = int(input("Enter the number of apples sold: "))
bananas_sold = int(input("Enter the number of bananas sold: "))

if apples_sold > bananas_sold:
    print("Apples had higher sales.")
elif apples_sold < bananas_sold:
    print("Bananas had higher sales.")
else:
    print("Sales were equal.")