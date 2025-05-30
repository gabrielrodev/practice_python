# input() = A function that prompts the user to enter data
#           Returns the entered data as a string

Name = input("What is your name?:")
age = int(input("How old are you?:")) # like this

#age = int(age) instead of doing this extra step we could do it in the input section
age += 1 # this will only work if we convert it into a int instead of a string


print(f"Hi {Name}")
print("Happy birthday!")
print(f"You are {age}")