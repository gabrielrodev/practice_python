# Python credit card validator
#1. Remove any '-' or ' '
#2. add all digits in the odd places from right to left
#3. Double every second digit from right to left.
#       (If result is a two-digit number,
#        add the two-digit number together to get a single digit.)
#4. Sum the totals of steps 2 & 3
#5. If sum is divisible by 10, the credit card # is valid
"""
sum_odd_digits = 0
sum_even_digits = 0
total_sum = 0

#Step 1
card_number = input("Enter a credit card #: ")

card_number = card_number.replace(" ", "")
card_number = card_number.replace("-", "")
card_number = card_number[::-1]

#Step 2
for card in card_number[::2]:
    sum_odd_digits += int(card)

#Step 3
for card in card_number[1::2]:
    card = int(card) * 2
    if card >= 10:
        sum_even_digits += (1 + (card % 10))
    else:
        sum_even_digits += card

#Step 4
total = sum_odd_digits + sum_even_digits

#Step 5
if total % 10 == 0:
    print("Valid")
else:
    print("Invalid")
"""

#what I did

sum_odd_digits = 0
sum_even_digits = 0
total_sum = 0

#Step 1

card_number = input("Enter a card number: ")
card_number = card_number.replace(" ", "")
card_number = card_number.replace("-", "")
card_number = card_number[::-1]
#Step 2
for card in card_number[::2]:
    sum_odd_digits += int(card)

#Step 3

for card in card_number[1::2]:
    card = int(card) * 2
    if card >= 10:
        sum_even_digits += (card // 10) + (card % 10) #gets up(// divides and takes out decimal places) and one down ( 10 leaves the remaider which always would be the first digit)
    else: 
        sum_even_digits += card


total_sum = sum_odd_digits + sum_even_digits

if total_sum % 10 == 0:
    print(f"{card_number} IS VALID")
else:
    print(f"{card_number} IS NOT VALID")


