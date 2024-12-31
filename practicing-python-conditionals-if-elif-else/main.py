print("Hello, World!")

# Syntax of the IF conditional
# Conditionals are structures that allow us to execute different code blocks depending on whether a condition is `true or false`.

expression = True

if expression: # <----------------------------------------- # The colon is mandatory
    print("Condition is True")  # follow this path
else: # <-------------------------------------------------- # The `else` block is optional. It is evaluated only if the `if` condition returns false.
    print("Condition is False")  # follow this other path

# Code Example
# This example prints a message on the screen if the company name is Alura.

name = "Alura" # <----------------------------------------- # First, we create a variable that stores the name "Alura".

if name == "Alura": # <------------------------------------ # As a condition for the `if` statement, we check if the variable value equals "Alura".
    print("Welcome")                                        # If so, we print the message "Welcome".

# Code Example
# Let's change the value assigned to the name variable to see what happens.

name = "Start"                 # |
                               # |  <---------------------- # When running the code again, nothing happens because the condition is false.
if name == "Alura":            # |                          # The `name` is not equal to "Alura", so nothing is printed to the screen.
    print("Welcome")           # |

# Code Example
# To make something happen when the condition is false, we need to `use the else block`.

name = "Start"                 # |
                               # |
if name == "Alura":            # |  <---------------------- # Now, the message "Unknown name" is printed.
    print("Welcome")           # |                          # If you change the value of `name` to anything other than "Alura",
else:                          # |                          # the `else` message will be displayed.
    print("Unknown name")      # |

# Code Example
# But what if we want to check for other names besides "Alura"? That's where `elif` comes into play.

name = "Alura"

if name == "Alura":
    print("Welcome to Alura!")
elif name == "Latam": # <---------------------------------- # The `elif` allows us to add a new condition to be checked before going to else.
    print("Welcome to Latam!")                              # In this example, if `name` equals "Alura", the message "Welcome to Alura!" is printed.
else:                                                       # If we change `name` to "Latam", "Welcome to Latam!" is displayed; otherwise,
    print("Unknown name.")                                  # the message "Unknown name" is shown.

# Comparison Operators
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


# Logical Operators
# When using conditional structures, it is common to need logical operators to combine multiple conditions. 
# The most common operators in Python are:

# - `and`: returns true only if all conditions are true.
# - `or`: returns true if at least one condition is true.

# +--------------------------------------+   +--------------------------------------+
# |             AND Operator             | - |              OR Operator             |
# +--------------------------------------+ - +--------------------------------------+
# | Condition 1 | Condition 2 | Result   | - | Condition 1 | Condition 2 | Result   |
# | True        | True        | True     | - | True        | True        | True     |
# | True        | False       | False    | - | True        | False       | True     |
# | False       | True        | False    | - | False       | True        | True     |
# | False       | False       | False    | - | False       | False       | False    |
# +--------------------------------------+   +--------------------------------------+

# Code Example AND
age = int(input("Enter your age: "))
has_document = input("Do you have a document? (yes/no): ")

if age >= 18 and has_document == "yes": # <---------------- # If both conditions are met, entry is allowed.
    print("Entry allowed!")                                 # Otherwise, it is denied.
else:                                                       # You can combine as many conditions as you want.
    print("Entry denied.")

# Code Example OR
holiday = input("Is it a holiday today? (yes/no): ")
leave = input("Do you have leave today? (yes/no): ")

if holiday == "yes" or leave == "yes": # <----------------- # In the example, if both answers are "no",
    print("You can rest today!")                            # the user will have a normal workday.
else:                                                       # But if it's a holiday OR they have leave,
    print("Normal workday.")                                # "You can rest today!" is printed.