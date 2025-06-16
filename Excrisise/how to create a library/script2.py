from script1 import * # reminder that * means everything in this case
# so the name __main__ is used to check if you are running the code from the same place were you are or if you are importing
# if you are importing you will get a weird

def favorite_drink(drink):
    print(f"your favorite drink is {drink}")
def main():
    print("this is script 2")
    favorite_drink("coffe")
    favorite_food("sushi")
    print("bye hoodie")

if __name__ == "__main__":
    main()