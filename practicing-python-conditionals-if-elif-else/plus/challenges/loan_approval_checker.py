"""
Pedro wants to apply for a loan, but approval depends on two conditions:

- The monthly income must be greater than $2,000.00.
- The installment amount cannot exceed 30% of the income.

Create a program that takes Pedro's monthly income and the desired installment amount as input.
The program should inform whether the loan is approved or denied based on the conditions above.

Expected output:
Enter your monthly income: 2500
Enter the desired installment amount: 800
Loan denied: Installment exceeds 30% of income.
"""

income = float(input("Enter your monthly income: "))
installment = float(input("Enter the desired installment amount: "))

if income > 2000 and installment <= 0.3 * income:
    print("Loan approved!")
elif income <= 2000:
    print("Loan denied: insufficient income.")
else:
    print("Loan denied: installment exceeds 30% of income.")