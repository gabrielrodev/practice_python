# iterables = An object/collection that can return its elements one at a time,
#              allowing it to be iterated over in a loop
"""
fruits = {"apple","orange", "bannana", "coconut"} #list, tuples are iterables ()
# {} sets can't be replace

for fruit in fruits: # this is iterable numbers
    print(fruit, end=" - ")
"""
"""
name = "Gabohappy" # this is cool you can separate leters in a string. i think there was something else that you can do in this type of cases

for character in name:
    print(character, end=" ")
"""

my_dictionary = {"A": 1,
                 "B": 2,
                 "C": 3,
                 "D": 4}
for key,values in my_dictionary.items():  #.values() for values, .key() for keys, .items for keys and values
    print(f"{key} = {values}")