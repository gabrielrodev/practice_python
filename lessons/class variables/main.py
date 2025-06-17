# class variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class

class Student:

    class_year = 2025
    num_students = 0


    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1 # when doing changes we need to start with the class name

student1 = Student("spongebob", 30)
student2 = Student("Harrypop", 14)
student3 = Student("Rockefeller", 65)
student4 = Student("max",13)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
#print(Student.class_year) # good practice to access class variable with the name of the class


#print(Student.num_students)
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)
