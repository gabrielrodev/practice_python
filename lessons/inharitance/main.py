# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class child(parent)
#                     sub(superclasses)

class Animal:

    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is Asleep")

class Dog(Animal):
    def speak(self):
        print("Woof!")
class Cat(Animal):
    def speak(self):
        print("Meow!")
class Mouse(Animal):
    def speak(self):
        print("Squeek!")

dog = Dog("Scooby")
cat = Cat("Garfiel")
mouse = Mouse("Ratatouille")

#print(mouse.name)
#print(mouse.is_alive)
#mouse.eat()
#mouse.sleep()

mouse.speak()