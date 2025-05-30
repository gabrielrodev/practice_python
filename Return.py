# return = ends the function and returns the result


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last


full_name = create_name("Dangers", "heart")

print(full_name)















"""
def add(x,y):
    z = x + y
    return z

def subtract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(1,2))
print(subtract(1,2))
print(multiply(1,2))
print(divide(1,2))
"""