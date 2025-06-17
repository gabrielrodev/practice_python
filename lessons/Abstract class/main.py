# Abstract class: A class that cannot be instantiated on its own; Meant to be subclassed.
#                 They can contain abstract methods, which are declared but have no implementation.
#                 Abstract classes benefits:
#                 1. Prevents instantiation of the class itself
#                 2. Requires children ot use inherited abstract methods

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass



class Car(Vehicle): # you need to include abstract methods

    def go(self):
        print('You started the automobile')

    def stop(self):
        print('You stopped the automobile')

class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("You stop the motorcycle")

class Boat(Vehicle):

    def go(self):
        print("You sail your boat")

    def stop(self):
        print("You anchor the boat")

boat = Boat()

boat.go()
boat.stop()

