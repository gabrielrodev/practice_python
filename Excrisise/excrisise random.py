import random

low = 1
high = 100
guesses = 0

number = random.randint(low, high)

while True:
    guess = int(input(f"Enter a number between ({low} and {high}): "))
    guesses += 1

    if guess < number:
        print(f"{guess} is too low")
    elif guess > number:
        print(f"{guess} is too high")
    else:
        print()
        print(f"{guess} is correct!")
        break
print(f"This round took you {guesses} guesses")