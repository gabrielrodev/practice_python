# Membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#                        1. in
#                        2. not in



email = "botijlv@gmail.com"
if "@" in email and "." in email:
    print("valid email")
else:
    print("invalid email")


"""
grades = { "Sandy":"A",
           "spongebob":"B",
            "rick": "C"}

student = input("Enter your name: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")
"""
"""
students = {"bob", "rick", "sandy"}

student = input("Enter a student name: ")

if student in students:
    print(f"welcome {student}")
else:
    print(f"Sorry {student} is not in the list")
"""
"""
word = "APPLE"

letter = input("Guess the letter in the secret word: ")

if letter.upper() not in word:
    print(f"{letter} was not found")
else:
    print(f"there is an {letter}")
"""