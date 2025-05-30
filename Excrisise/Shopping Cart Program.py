
item = input("Enter your item name: ")
price = float(input("Enter your item price: "))
quantity = int(input("Enter your item quantity: "))

total_price = price * quantity

if item == "Gabohappy" or item == "gabohappy":
    print("priceless")
else:
    print(f"You have bought x{quantity} {item} ")
    print(f"Your total price is ${total_price}")