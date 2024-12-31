"""
Camila is organizing a project and needs to calculate the total time required to complete three activities: A, B, and C.
However, if any activity has a negative number of days, the program should warn that the entered values are invalid and not calculate the total.

Write a program that receives the number of days for three activities and displays the total project time.
If any value is negative, display an error message.

Expected output:
Enter the days for activity A: 5
Enter the days for activity B: -8
Enter the days for activity C: 10
Error: Days cannot be negative.
"""

activity_A = int(input("Enter the days for activity A: "))
activity_B = int(input("Enter the days for activity B: "))
activity_C = int(input("Enter the days for activity C: "))

if activity_A < 0 or activity_B < 0 or activity_C < 0:
    print("Error: Days cannot be negative.")
else:
    total_time = activity_A + activity_B + activity_C
    print(f"The total project time is {total_time} days.")