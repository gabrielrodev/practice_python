# Collection = single "variable" used to store multiple values
#   List = [] ordered and changeable. Duplicates OK
#   Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. Faster

#                   !!!!!!!!!!!!!!!!!!!!LIST!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#fruits = ["apple","orange","banana","coconut"] # this is a collection of fruits so make it plural this is a list

#print(dir(fruits))  # gives you methods of a collection
#print(help(fruits)) # helps you understand what you are capable of with a list
#print(len(fruits)) # makes it so that we can see the length of a list
#print("apple" in fruits) # basically gives you a boolean expression, telling you that apple is in fruits and if it's not it's going ot give you a false as response
#fruits[0] = "pineapple" # changes the value mentioned in the index for the new string or value
#fruits.append("pineapple") # adds an element to the end of the list
#fruits.remove("apple") # adds an apple
#fruits.insert(1,"pineapple") #inserts a new element like little inserts it, it does not change the others
#fruits.sort() #sorts by alphabetical order
#fruits.reverse() # reverse the list, as you put it not in alphabetical order
#fruits.clear() # deletes all the elements in a list
#print(fruits.index("apple")) #asks for what index is a certain object on the list on
#print(fruits.count("coconut")) # counts how many objects on the list there are

                            #new skill unlocked shift + enter skips to the next line no matter where you are
#print(fruits)


#Fun fact
#fruit is also plural
#print(fruits[::-1]) #to access you can use [] index operator.

#for fruit in fruits:      #I still don't quite understand for loops but like i get it a little more
    #print(fruit)           #If we look close we are using fruit as the new variable of singular of the plural fruits
#                          # which would make a lot of since and explains why we create a variable on the first place


#            !!!!!!!!!!!!!!!!!!SETS!!!!!!!!!!!!!!!!!!!!!!
#fruits = {"apple","orange","banana","coconut"} # unordered and can't be change, add/remove OK. No duplicates

#print(dir(fruits))  # gives you methods of a collection
#print(help(fruits)) # helps you understand what you are capable of with a list
#print(len(fruits)) # makes it so that we can see the length of a list
#print("apple" in fruits) # basically gives you a boolean expression, telling you that apple is in fruits and if it's not it's going ot give you a false as response
# Can't use indexing
#fruits.add ("pineapple") # add element
#fruits.remove("apple") # remove selected element
#fruits.pop() # you can remove the first random element
#fruits.clear() # you can clear elements

#                   !!!!!!!!!!!!!!!!!!!!TUPLE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
fruits = ("apple","orange","banana","coconut") #can have duplicate but can't be change

#print(dir(fruits))  # gives you methods of a collection
#print(help(fruits)) # helps you understand what you are capable of with a list
#print(len(fruits)) # makes it so that we can see the length of a list
#print("apple" in fruits) # basically gives you a boolean expression, telling you that apple is in fruits and if it's not it's going ot give you a false as response
#print(fruits.index("apple"))
#print(fruits.count("coconut"))

for fruit in fruits:
    print(fruit)
