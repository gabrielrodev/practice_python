# Reduce(function, collection) = Reduces elements in a collection to a single value
#                                For loop is better in most cases
#                                Reduce os better fpr a functional approach + readability
# Is like sum function

from functools import reduce

prices = [10.23,23.1,48.45,49.75,40.54,34.85,24.98,54.09,78.3]

total = reduce(lambda x,y: x + y, prices)

print(f"${total}")