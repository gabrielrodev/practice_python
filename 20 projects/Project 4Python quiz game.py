# Python quiz game

questions = ("How many elements are in periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas?",
             "What is the biggest planet known?",
             "what is my favorite color?",
             )

options = (("A. 116","B. 117","C. 118","D. 119"),
           ("A. Whale","B. Crocodile","C. Elephant","D. Ostrich"),
           ("A. Nitrogen","B. Oxygen","C. Carbon-Dioxide","D. Hydrogen"),
           ("A. Jupiter","B. Earth","C. TRES-4","D. Saturn"),
           ("A. Blue","B. Green","C. Purple","D. Yellow"))

answers = ("C","D","A","C","B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter your response (A,B,C,D): ").upper() # make the user input uppercase
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"answers {answers[question_num]} is the correct answers")
    question_num += 1

print("----------------")
print("     RESULTS    ")
print("----------------")

print("answers:", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses:", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score/ len(questions) * 100)

print(f"Your score is {score}%")