# Sorting in python .sort() or sorted()
# Lists[], Tuples(), Dictionaries{"":""}, Objects

#.sort sorts from a to z or from least to biggest
#to reverse it .sort(reverse=True)

# ------------- LISTS -------------

#fruits = ['apple', 'banana', 'cherry','coconut', 'tangerine','orange']
#numbers = [1,4,5,6,3,7]
#numbers.sort(reverse=True)

#print(numbers)

# ------------- TUPLES -------------

#fruits = ('apple', 'banana', 'cherry','coconut', 'tangerine','orange')

#fruits = tuple(sorted(fruits))
#fruits = tuple(sorted(fruits, reverse=True))

#print(fruits)

# ------------- DICTIONARIES -------------


#fruits = {'apple':72, 'banana':100, 'cherry':87,'coconut':354, 'tangerine': 47,'orange':73}

#fruits = dict(sorted(fruits.items()))
#fruits = dict(sorted(fruits.items(), key=lambda item: item[0], reverse=True))
#fruits = dict(sorted(fruits.items(), key=lambda item: item[1], reverse=True))
#print(fruits)

# ------------- OBJECTS -------------

class Fruit:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def __repr__(self):
        return f"{self.name}: {self.calories}"

fruits = [Fruit("banana", 105),
          Fruit("apple", 72),
          Fruit("orange", 80),
          Fruit("coconut", 354)]

#fruits = sorted(fruits, key=lambda fruit: fruit.name)
#fruits = sorted(fruits, key=lambda fruit: fruit.name, reverse=True)
fruits = sorted(fruits, key=lambda fruit: fruit.calories, reverse=True)

print(fruits)