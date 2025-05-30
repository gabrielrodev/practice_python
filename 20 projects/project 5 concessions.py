menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda":3.00,
        "lemonade" : 4.25
        }
cart = []
total = 0

print("------ MENU ------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("------------------")

while True:
    food = input("What do you want to buy?(q to quit):")
    if food.lower() == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("----- YOUR ORDER -----")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is {total:.2f}")
print("----------------------")

"""

prices = { "popcorn" : 1.00,
           "hotdog" : 2.00,
           "pretzel" : 2.00,
           "candy" : 1.00,
           "soda" : 1.00,
           "water" : 1.00
}
cart =[]
total = 0

print("_______MENU_________")
for key, value in prices.items():
    print(f"{key:10} = ${value}")
print()
while True:
    item = input("What item would you like to order first(q to quit):")
    cart.append(item)
    if item.lower() == "q":
        print("Thanks for shopping!")
        break
    else:
        total = total + prices[item]
        print(total)

print(f"Your total was {total}. You order is {cart} ")
"""