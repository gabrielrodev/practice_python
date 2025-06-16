# 2D lists, list made of lists

"""
you can also
groceries = [["apple","orange","banana","coconut"],["celery", "carrots","potatoes"],["chicken", "fish", "turkey"]] # we can make toples insides sets ({})

print(groceries)
"""
fruits =    ["apple","orange","banana","coconut"]
vegetable = ["celery", "carrots","potatoes"]
meats =     ["chicken", "fish", "turkey"] # you can also do toples

groceries = [fruits,vegetable,meats]


for collection in groceries:   # THIS IS CALLED NESTED LOOPS
    for food in collection:
        print(food, end=" ")
    print()
#print(groceries[1][0]) #returns entire lists if its does not have two indexis. row 0