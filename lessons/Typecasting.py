# Typecasting = the process of converting a variable from one data type to another
#               str(), int(), float(), bool()

name = "Gabo happy"
age = 18
gpa = 3.2
is_student = True
# type is to find the type of data type of the variable, we put it inside print to show us the return from type function


"""
 If the name has nothing inside the boolean expression will be false if anything is inside the name then it will be true
name = bool(name)

print(name)

OUTPUT 

true
"""



"""
#NOTE age += 1 is the same as age = age + 1 
 Even when the result is the same, it is a string and not a integer
 if we were to try adding one to age it will no longer work because it is a string now and it will give a TypeError
 
 you can add a string to a string by doing age += "1" which will give you the OUTPUT of 181
age = str(age)

print(age)
print(type(age))

OUTPUT
18 
str
"""

"""
 As expected when doing a integer to a float it is just going to display the place holder decimal
age = float(age)

print(age)
OUTPUT
18.0
"""

"""
 because we converted this the gpa just took out the decimals of the float number in the output
gpa = int(gpa)

print(gpa)

OUTPUT 
3
"""