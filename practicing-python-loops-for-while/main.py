print("Hello, World!")

# What are loops?
# Loops are structures that allow you to execute a block of code repeatedly while a condition is true.
# Types of loops in Python:
# - `For`
# - `While`
# A loop can be interpreted as: repeat until the condition becomes false.
# ♾️ Is it true? If yes, repeat...

# Syntax of the FOR loop
# The for loop is used to execute a block of code for each element in the iterable.
# It is useful when you know exactly how many iterations you want to perform.

# Example of a collection of values.
iterable = [1, 2, 3, 4, 5] # 🡠------- This is a collection of values, such as lists, tuples, dictionaries, among others.

# Each individual item of the iterable that is processed inside the loop (Here, 'element' represents each item within the iterable's collection of values).
#      🡣
for element in iterable:  # 🡠------ The colon and the word `in` are mandatory.
    print(element) # Block of code executed for each item.

# Example of a FOR loop code
# This example iterates over a list of names and prints each one on the screen.

names = ["Carlos", "Ana", "Pedro", "Maria"] # 🡠---- First, we create a list called `names` that contains the names: `["Carlos", "Ana", "Pedro", "Maria"]`.

#  The term "name" is just an identifier we use to represent each element of the list as we iterate with the for loop.
#  You can replace "name" with any other variable name that makes sense in your context.
#    🡣
for name in names: # 🡠--------- Next, we use a `for` loop to iterate through all the names in the list and print each name on the screen.
    print(name)

# Syntax of the WHILE loop
# The while loop executes a block of code as long as a specified condition is true.
# It is useful when you don't know exactly how many iterations will be necessary,
# as the execution depends on the condition's result at each iteration.

condition = False

while condition: # 🡠------------------- The condition is any expression that evaluates to a boolean value (True or False). Example: while number < 5
    print(". . .") # Block of code

# Comparison Operators
# Comparison operators are used to compare values, returning True or False depending on the condition established.

# +-----------------------+----------------------------------------------------+---------+
# |       Operator        |                       Concept                      | Example |
# +-----------------------+----------------------------------------------------+---------+
# | > (Greater than)      | Checks if one value is greater than another        | x > 10  |
# | < (Less than)         | Checks if one value is less than another           | x < 10  |
# | == (Equal to)         | Checks if one value equals another                 | x == 10 |
# | != (Not equal to)     | Checks if one value is not equal to another        | x != 10 |
# | >= (Greater or equal) | Checks if one value is greater or equal to another | x >= 10 |
# | <= (Less or equal)    | Checks if one value is less or equal to another    | x <= 10 |
# +-----------------------+----------------------------------------------------+---------+

# Example of WHILE loop code
# This example iterates through a list of names and prints each one on the screen.

# We define a variable "counter" with the value 0.
# The counter ensures that the condition eventually becomes false.
counter = 0

while counter < 5:
    # The while loop checks the condition counter < 5.
    # As long as this condition is true, the block of code inside the while will be executed.
    print(f"Current counter: {counter}")

    # Inside the loop, we print the current value of the counter and
    # then increment the counter by 1 with counter += 1.
    # This process repeats until the condition counter < 5 becomes false
    # (i.e., when the counter reaches 5).
    counter += 1

# Note:
# Python does not have the increment (++) or decrement (--) operators found in other languages.
# Instead, we use the compound assignment operator '+=', which is a Pythonic way to increment values.

# Infinite Loop
# An infinite loop occurs when a loop continues to execute indefinitely
# because the condition to exit it never becomes false.
"""
infinite_loop = 0

while infinite_loop < 5: # 🡠------------------- In this example, the loop will continue forever, printing "Infinite Loop: 0" because the condition infinite_loop < 5 will never change to false.
                                                 # This can happen in both for and while loops.
    print(f"Infinite Loop: {infinite_loop}")

Warning:
The example above is an infinite loop, meaning it will continue to execute indefinitely because the condition is never updated.
Do not execute this code without modifying it, as it may freeze the program or the environment where it is running.
This example is purely educational to illustrate the concept. To avoid infinite loops, always ensure the loop's condition will eventually become false.
"""

# Break
# What if we want to interrupt the execution of a loop before it naturally ends?
# This is where the break statement comes into play. The break allows you to exit a loop immediately,
# even if the condition to continue is still true.

users = ["PM3", "Alura", "Latam", "Others"]

for user in users:
    if user == "Alura":
        print("User found! Exiting the loop.")
        break # 🡠-------------------------------------- In this example, the loop will iterate through the names, and upon finding "Alura",
                                                        # it will print "User found! Exiting the loop." and exit the loop, not printing the subsequent names.
    print(user)

# Continue
# Now, what if we want to skip the execution of a specific iteration of the loop
# but continue with the rest?
# The `continue` command allows you to jump to the next iteration of the loop, ignoring the rest of the code in the current iteration.

nicknames = ["PM3", "Alura", "Latam", "Others"]

for nickname in nicknames:
    if nickname == "Alura":
        print("Ignoring Alura.")
        continue
    print(f"Nickname: {nickname}")

# Useful functions in loops

# - len() is used to get the length of a list, string, or another type of collection.
# It allows us to determine how many iterations we need to perform in a loop.

# - range() generates a sequence of numbers, which is often used to control iteration in for loops.
# With it, we can specify a range of numbers to iterate, and we can also define a step.
# For example, range(6) generates the numbers from 0 to 5, allowing the for loop to execute five times.