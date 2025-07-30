# Static methods: A method that belong to a class rather than any object from that class(instance)
#                 Usually used for general utility functions
#
# Instance methods = Best for operations on instances of the class (objects) (probably the thing you get when retriving a mthod of an object(object is the def or storage i think)
# Static methods = best for utility functions that do not need access to class data
# Method is a function which is a member of a class

class Employee: #(object)

    def __init__(self, name, position): #constructor
        self.name = name  #are we creating this to store or to place hold the name variable.
        self.position = position

    def get_info(self):   # this is an instance method, each object that we create will have their own get_info method
        return f"Employee: {self.name}, position: {self.position}"

    @staticmethod       #static method we need a decorator
    def is_valid_position(position):
        valid_position = ["GameDev", "SoftwareDev", "Cybersecurity", "FrontEndEngineer"]
        return position in valid_position




employee1 = Employee("John", "psychiatrist")  #this is how you will call an instance method
employee2 = Employee("Mary", "GameDev")
employee3 = Employee("Cris","SoftwareDev" )

# for static positions we don't need to do employee1 = Employee(name, position)
print(Employee.is_valid_position("GameDev"))
#this is how you will call an instance method
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())


"""class C:
def method(self, possibly, other, arguments): 
    pass # do something here"""

# any def get_info is a method
# def __init__(self,name) is a dunder method

#NOTES
"""STATIC METHODS: static methods belong to the classes not actually the methods or def under them only to the class
"""