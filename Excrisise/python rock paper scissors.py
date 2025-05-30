import random


options = ("rock", "paper", "scissors")
game = True
print("-----------------------------------------")
print("---Welcome to Rock Paper Scissors game---")
print("-----------------------------------------")
print()
while game:

    player = None
    computer = random.choice(options)

    while player not in options:



        player = input("Enter your choice (rock, paper, scissors): ").lower()

    print(f"player: {player}")
    print(f"computer: {computer}")
    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You have won")
    elif player == "paper" and computer == "rock":
        print("You have won")
    elif player == "scissors" and computer == "paper":
        print("You have won")
    else:
        print("You lose")

    if not input("Play again? (y/n): ").lower() == "y":
        game = False

print("Thanks for playing")