"""
A teacher needs a program to calculate the final average of students and determine if they are approved, on recovery, or failed.

Rules:
- Average >= 7: Approved
- 5 <= Average < 7: Recovery
- Average < 5: Failed

Write a program that takes three grades as input and calculates the final average. Based on the average, display the student's status.

Expected output:

Enter the first grade: 5.3
Enter the second grade: 6.7
Enter the third grade: 8.3
Average: 6.77
Recovery
"""

first_grade = float(input("Enter the first grade: "))
second_grade = float(input("Enter the second grade: "))
third_grade = float(input("Enter the third grade: "))

average = (first_grade + second_grade + third_grade) / 3

print(f"Average: {average:.2f}")

if average >= 7:
    print("Approved")
elif 5 <= average < 7:
    print("Recovery")
else:
    print("Failed")
