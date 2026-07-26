Password Generator  (Python Programming Project 3)

A secure command line random password generator built in Python, completed as Project 3 during my Python Programming training at DecodeLabs.

About

This project focuses on secure randomness and string manipulation. Instead of using Python's regular "random" module (which is predictable and not secure enough for passwords), this program uses the "secrets" module, which is the correct choice for generating passwords and security tokens.

Features

Asks the user for a desired password length
Validates input - rejects lengths under 4 characters
Validates input - rejects non-numeric entries
Generates a secure random password using letters and digits

Concepts Used

secrets module (cryptographically secure randomness, safer than random)
string module (string.ascii_letters, string.digits)
String building with join() for efficiency
Input validation with try/except
while loop with continue and break

How to Run

1. Make sure you have Python installed (python.org/downloads)
2. Clone this repository: git clone https://github.com/dayod4606-tech/password-generator-python.git
3. Navigate into the folder: cd password-generator-python
4. Run the program: python password_generator.py

Example Usage

--- PASSWORD GENERATOR ---
Enter password length (12): 2
Please choose a length of at least 4.
Enter password length (12): abc
That's not a number. Try again.
Enter password length (12): 16

Your generated password: l1eK5Ol58xsRDw95

Training Program

Part of the Python Programming Industrial Training  Batch 2026, powered by DecodeLabs.

Built as part of my Python Programming learning journey.
