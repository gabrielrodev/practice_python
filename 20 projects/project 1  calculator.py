# Python calculator

operator = input("Enter an operator (+ - * /): ")
a = float(input("enter first number:"))
b = float(input("enter second number:"))
if operator == "+":
    result = a + b
    print(f"The answer is: {round(result,3)}")
elif operator == "-":
    result = a - b
    print(f"The answer is: {round(result,3)}")
elif operator == "*":
    result = a + b
    print(f"The answer is: {round(result,3)}")
elif operator == "/":
    result = a / b
    print(f"The answer is: {round(result,3)}")
else:
    print(f"invalid operator {operator}")
