# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits


username = input("Enter username: ")

if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("username can't contain any numbers")
else:
    print(f"Welcome {username}")







#my answer
"""
username = input("Please enter your username(less than 12 characters, no spaces, no digits): ")

if len(username) <= 12 and username.isalpha():
    print(f"Your username is {username}")
else:
    print("invalid username")
"""