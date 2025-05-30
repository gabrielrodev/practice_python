#indexing = accessing elements of a sequence using [] (indexing operator)
#           [start : end : step]
#         Inclusive exclusive
#print(credit_number[0]) # you can write the index of the number you want to print
#print(credit_number[:4]) you can write [:4]
#print(credit_number[5:9])
#print(credit_number[5:])
#print(credit_number[-1]) you can use negative index
#print(credit_number[::3]) #count every 4 character
credit_number = "1234-5678-9012-3456"

credit_number = credit_number[::-1] #inverses the string

print(credit_number)
#last_digits = credit_number[-4:]
#print(f"XXXX-XXXX-XXXX-{last_digits}")