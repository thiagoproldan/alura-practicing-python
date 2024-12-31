"""
Carlos wants to monitor his monthly budget to avoid overspending.
He has set a limit of $3,000.00 for his expenses and needs a program to help control his spending.
The program should receive the total expenses and inform whether he has exceeded the limit or is still within the budget.

Expected output:
Enter the total monthly expenses ($): 5897.58
Warning! You have exceeded the monthly budget limit.
"""

expense_limit = 3000.0
total_expenses = float(input("Enter the total monthly expenses ($): "))

if total_expenses > expense_limit:
    print("Warning! You have exceeded the monthly budget limit.")
else:
    print("You are within the monthly budget.")