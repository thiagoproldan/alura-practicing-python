"""
Anna Júlia is creating a system to calculate the Body Mass Index (BMI) and provide basic recommendations.
The program should receive a person's weight and height, display the BMI value, and indicate if they are underweight, normal weight, overweight, or obese.
Create a program that receives the weight (in kg) and height (in meters) and calculates the BMI using the formula: BMI = weight / (height ** 2).
Then, display the BMI value and a message indicating if the person is underweight (BMI < 18.5), normal weight (18.5 <= BMI < 25), overweight (25 <= BMI < 30), or obese (BMI >= 30).

Expected output:
Enter your weight (kg): 75
Enter your height (m): 1.68
Your BMI is: 26.57
You are overweight.
"""

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

bmi = weight / (height ** 2)  # Weight (kg) / Height (m)^2
print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 25:  # Chained comparison
    print("You are at a normal weight.")
elif 25 <= bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")