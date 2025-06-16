# python banking program

def show_balance(balance):
    print("*******************")
    print(f"Your balance is ${balance:.2f}") #format specifiers
    print("*******************")

def deposit():
    print("*******************")
    amount = float(input("Enter amount to deposit: "))
    print("*******************")
    if amount < 0:
        print("*******************")
        print("That's not a valid amount")
        print("*******************")
        return 0
    else:
        return amount # has to do this step

def withdraw(balance):
    print("*******************")
    amount = float(input("Enter amount to withdraw: "))
    print("*******************")
    if amount > balance:
        print("*******************")
        print("Not enough funds")
        print("*******************")
        return 0
    elif amount < 0:
        print("*******************")
        print("Amount must be greater than 0")
        print("*******************")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("*******************")
        print("  Banking Program")
        print("*******************")
        print(f"1. Show balance")
        print(f"2. Deposit")
        print(f"3. Withdraw")
        print(f"4. Exit")
        print("*******************")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("*******************")
            print("That is not a valid choice")
            print("*******************")

    print("*******************")
    print("Thank you! Have a nice day.")
    print("*******************")
if __name__ == "__main__": #it makes your program so that you can use it in another project
    main()

"""
balance = 0
while True:
    user_input_menu = input("Select and option: ")
    print(f"1. Show balance")
    print(f"2. Deposit")
    print(f"3. Withdraw")
    print(f"4. Exit")

    if user_input_menu == "1":
        print(f"Balance: {balance}")
    elif user_input_menu == "2":
        deposit = float(input("How much would you like to deposit: "))
        balance += deposit
        print(f"You have deposited {deposit}.")
    elif user_input_menu == "3":
        withdraw = float(input("How much would you like to withdraw: "))
        balance -= withdraw
        print(f"You have withdrawn {withdraw}.")
    elif user_input_menu == "4":
        print("Thank you for using our bank!")
        break
"""