"""
Fernanda is planning a trip and wants to calculate how much she will pay in tolls.

The toll fee depends on the distance traveled:
- Up to 100 km: $10.00
- Between 100 km and 200 km: $20.00
- Above 200 km: $30.00

Create a program that takes the distance traveled and outputs the corresponding toll fee.

Expected output:
Enter the distance traveled (in km): 250
Toll fee: $30.00
"""

distance_traveled = int(input("Enter the distance traveled (in km): "))

if distance_traveled <= 100:
    print("Toll fee: $10.00")
elif distance_traveled <= 200:
    print("Toll fee: $20.00")
else:
    print("Toll fee: $30.00")