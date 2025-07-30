# Class Methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself
# Instance methods = Take (self), Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data
# Class methods = Best for class-level data or require access to the class itself

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa): # this is an instance method
        self.name = name #are we creating this to store or to place hold the name variable?
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # instance method
    def get_info(self):
        return f"Student: {self.name}|GPA: {self.gpa}"

    @classmethod   #class methods
    def get_count(cls):
        return f"Total of students: {cls.count}"

    @classmethod   # this is a method decorator @
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average GPA: {cls.total_gpa / cls.count:.2f}" # this is called a format specifier :.2f

student1 = Student("Bob", 3.1)
student2 = Student("Alice", 2.3)
student3 = Student("Rom", 5.0)


print(Student.get_count())
print(Student.get_average_gpa())



# if__name__ = __main__ (what whas the idea behind this?)