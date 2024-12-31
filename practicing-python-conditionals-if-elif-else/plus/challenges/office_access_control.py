"""
Mariana is responsible for granting access to the office and needs a program to check if employees can enter.
For this, she will use the current time. The office only allows access between 8 AM and 6 PM.
Create a program that receives the current time as input (in 24-hour format) and displays a message indicating whether access is allowed or denied.

Expected output:
Enter the current time (in 24-hour format - 0 to 23): 21
Access denied.
"""

current_hour = int(input("Enter the current time (in 24-hour format - 0 to 23): "))

if 8 <= current_hour < 18: # Office hours: Start at 8 AM, end at 5:59 PM (18 not included)
    print("Access allowed.")
else:
    print("Access denied.")