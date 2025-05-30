# Variable = A container or a value (string, integer, float, boolean)
#            A variable bahaves as if it was the value it contains
from operator import truediv

# Strings: characters that can include numbers but we treat them as variables
first_name = "Gabohappy"
food = "sushi"
email = "boti@fake.com"

#Integers
age = 24 #can't be between quotes because it will be a string
quantity = 3 # Can't have 3.5 of something because it will be a float number or a double
num_of_students = 30

# Float
price = 10.99 # floats contain a decimal portion
gpa = 3.2
distance = 5.5

# Boolean
# only have two options true or false
is_student = False
for_sale = False
is_online= False

if is_online:
    print("You are online")
else:
    print("You are offline")


"""
if for_sale:
    print("That item is for sale")
else:
    print("that item is not available")


if is_student:
    print("You are a student!")
else:
    print("You are not a student")
"""
"""
print(f"The price is ${price} for a book a read")
print(f"Your gpa is: {gpa}")
print(f"You ran {distance}km")
"""


"""
print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")
"""

"""
print(f"Hello {first_name}") # you don't want to put the variable in quatations "" because it will make it literly write first_name
print(f"You like {food}")
print(f"Your email is {email}")
"""