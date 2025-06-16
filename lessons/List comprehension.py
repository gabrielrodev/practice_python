# List comprehension = A concise way to create lists in python
#                      compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]
#
import random

grades = [85,29,43,24,20,10,90]
passing_grades = [grade for grade in grades if grade >= 60] #the first grade is what we are returning

print(passing_grades)


"""numbers = [1,-2,3,-4,5,-6, 8, -7]
positive_nums = [num for num in numbers if num >=0]
negative_nums = [num for num in numbers if num <=0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]
print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)
"""

"""fruits = ["banana", "apple", "pear"]
fruit_chars = [fruit[0] for fruit in fruits]
print(fruit_chars)"""
"""doubles = [x * 2 for x in range(1,11)]
triples = [y * 3 for y in range(1,11)]
squares = [z * z for z in range(1,11)]
print(squares)"""