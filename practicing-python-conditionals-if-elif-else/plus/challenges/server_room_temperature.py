"""
Lucas works in IT and needs to ensure that the temperature of a server room does not exceed 25°C.
He wants a program that receives the current temperature as input and, if necessary, displays a warning message.

Expected output:
Enter the current temperature: 30
Warning! Temperature above the allowed limit.
"""

current_temperature = float(input("Enter the current temperature: "))

if current_temperature > 25:
    print("Warning! Temperature above the allowed limit.")
else:
    print("Temperature within the safe limit.")