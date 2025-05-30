import random

low = 1
high = 100
guesses = 0
answer = random.randint(low, high)
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {low} and {high} ")



while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low or  guess > high:
            print("That number is out of range")
            print(f"please enter a number between {low} and {high}")
        elif guess < answer:
            print("The number is to low")
        elif guess > answer:
            print("The number is to high")
        else:
            print(f"You guessed {answer} correctly")
            print(f"Number of guesses {guesses}")
            is_running = False

    else:
        print("Invalid guess")
        print(f"Please select a number between {low} and {high}")


