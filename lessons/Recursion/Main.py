# What I Think i'm going to learn with recursion, I think is something about repetition of some sort, it looks to be hard
# Recursion = a function that calls itself from within
#             helps to visualize a complex problem into basic steps,
#             which can be solved more easily iteratively or recursively

# Iterative FASTER

#def walk(steps):
#    for step in range(1, steps + 1):
#        print(f"You take step #{step}")

#Recursive SIMPLER TO WRITE

#def walk(steps):
    #if steps == 0:
    #    return
    #walk(steps - 1)
    #print(f"You take step #{steps}")


#walk(100)

# EXAMPLE TIME(here we will be getting the factorial of a number)

#INTERATIVE
#def factorial(x):
 #   result = 1
 #   if x > 0:
 #       for y in range(1, x+1):
#            result = result * y
#        return result

# RECURSIVE
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
print(factorial(10))