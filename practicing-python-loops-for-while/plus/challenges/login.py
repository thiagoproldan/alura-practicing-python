"""
João is developing a registration system for a reading website. He needs to ensure that users enter a valid username and password. The rules are as follows:

- The username must have at least 5 characters.
- The password must have at least 8 characters.

João wants the system to keep requesting information until both conditions are met. When the user enters valid data, the program should display the message: "Registration successful!".

Create a program that implements this logic using a while loop.

Expected output:
Enter a username: user
Enter a password: 123
The username must have at least 5 characters.
Enter a username: user22
Enter a password: 12345
The password must have at least 8 characters.
Enter a username: user22
Enter a password: 123456789
Registration successful!
"""

while True:
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    if len(username) < 5:
        print("The username must have at least 5 characters.")
        continue  # The `continue` causes the program to skip the remaining code in the current loop and start the next iteration.

    if len(password) < 8:
        print("The password must have at least 8 characters.")
        continue  # Here too, the `continue` skips the rest of the code below and goes back to requesting the inputs.

    print("Registration successful!")
    break  # The `break` exits the loop when the conditions are met.