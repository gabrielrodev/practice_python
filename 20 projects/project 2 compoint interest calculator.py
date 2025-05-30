# Python compound interest calculator

principle = 0
rate = 0
time = 0


while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than or equal to zero")
    else:
        break
while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate can't be less than or equal to zero")
    else:
        break
while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("time can't be less than or equal to zero")
    else:
        break

total = principle * pow((1 + rate / 100), time) #check the parenthesis it took you to much time time to understand that the problem was the formula and the parenthesis

print(f"Balance after {time} year/s: ${total:.2f}")




"""
FIRST METHOD

principle = 0
rate = 0
time = 0


while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle can't be less than or equal to zero")

while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Interest rate can't be less than or equal to zero")

while time <= 0:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("time can't be less than or equal to zero")

total = principle * pow((1 + rate / 100), time) #check the parenthesis it took you to much time time to understand that the problem was the formula and the parenthesis

print(f"Balance after {time} year/s: ${total:.2f}")
"""

"""
    rate = float(input("Enter interest rate: "))
    time = float(input("Enter time that has passed: "))

    Finial_amount = initial_balance(1+interest_rate/)
    quit = input("Enter any key to proceed (q to quit):")
"""