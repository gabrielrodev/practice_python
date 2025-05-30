# while loop = execute some code WHILE some condition remains true

"""
num = int(input("Eneter a # between 1 - 10 to grade your crush: "))
person = input("Enter the name of the special person you like: ")
while num < 1 or num > 10:
    print(f"{num} not valid")
    num = int(input("Enter a # between 1 - 10: "))

if num > 5:
    print(f"You love {person} {num} out of 10")
elif num <= 5:
    print(f"just a {num}? leave {person} alone. value more yourself!")

"""
"""
food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter a food you like (q to quit): ")

print("bye")
"""
"""
age = int(input("Enter your age:"))

while age < 0:
    print("Age can't be negative")
    age = int(input("enter your age:"))

print(f"You are {age} years old")
"""
"""
name = input("Enter your name: ")
while name == "":
        print("You did not enter your name")
        name = input("Enter your name: ")
print(f"Hello {name}")
"""