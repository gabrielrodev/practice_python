#P.O.O.P
#Python object, oriented, programming

# object = a "bundle" of related attributes (variables) and methods (functions)
#           Ex. phone, cup, book
#           You need a "class" to create many objects'

# A method is function that belongs to an object
# object is a bundle of related attributes( phone: turn on, turn off, call)  and methods

# A class is like is a type of blueprint use to design the structure and layout of an objects
#METHODS are actions that objects can preform


from car import Car



car1 = Car("toyota", "2025", "brownish", False)
car2 = Car("nissan","2023","green", True)
car3 = Car("bugatoo", "2024", "black", False)

car1.describe()


#print(car1.model) #atribute access operator
#print(car1.year)
#print(car1.color)
#print(car1.for_sale)