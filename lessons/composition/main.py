# Aggregation = A relationship where one object contains references to other INDEPENDENT objects(stores info that can preform actions)
#               "has-a" relationship
# def (creates a function)
# Composition = The composed object directly own its components, which cannot exist independently
#               "owns-a" relationship
# def can be a constructor
class Engine:
    def __init__ (self, horse_power):
        self.horse_power = horse_power

class Wheel:
    def __init__(self,size):
        self.size = size

class Car: # car class owns all the objects set
    def __init__(self,make,model, horse_power, wheel_size): #inside of the object there are attribute
        self.make = make
        self.model = model
        self.engine = Engine(horse_power)
        self.wheels = [Wheel(wheel_size) for wheel in range(4)]

    def display_car(self):
        return f"{self.make} {self.model} {self.engine.horse_power}(hp) {self.wheels[0].size}"

car1 = Car(make="Ford",model="nissan",horse_power= 500,wheel_size= 18)
car2 = Car(make="Bugatti", model="Veyron", horse_power= 1000, wheel_size= 26)

print(car1.display_car())
print(car2.display_car())