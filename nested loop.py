# nested loop = A looop within another loop (outer, inner)
#               outer loop:
#                   inner loop:

rows = int(input("Enter the # of rows:"))
columns = int(input("Enter the # of columns:"))
symbol = input ("Enter a symbol to use:")

for x in range (rows):
    for y in range(columns): #the counter variable of the outer loop has to be different from the one on the inner loop
        print(symbol, end="") #end = "" is to change it from the regular end = "/n" statement
    print()