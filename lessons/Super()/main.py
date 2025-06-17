# super() = Function used in a child class to call methods from a parent class (superclass).
#           Allows you to extend functionality the functionality of the inherited methods

class Shape:
    def __init__(self, color, is_filled,):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {"filled" if self.is_filled else "not filled"}.")


class Circle(Shape):
    def __init__(self,color, is_filled, radius):
        super().__init__(color, is_filled) # super() is like calling the class name of shape basically
        self.radius = radius

    def describe(self):
        super().describe()
        print(f"it is a circle with a area of {3.14 * self.radius * self.radius}cm^2.")


class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        super().describe()
        print(f"it is a square with a area of {self.width * self.width}cm^2.")
class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        super().describe()
        print(f"it is a triangle with a area of {self.width * self.height / 2}cm^2.")

circle = Circle('blue', True, 5) # you can add color= , is_filled=, radius= for redability if wanted
square = Square("green", False, 10)
triangle = Triangle("brown", True, 10, 25)

#print(f"{circle.color}.\n{circle.is_filled}.\n{circle.radius}")
#print()
#print(f"{square.color}.\n{square.is_filled}\n{square.width}cm.")
#print()
#print(f"{triangle.color}.\n{triangle.is_filled}.\n{triangle.width}cm.\n{triangle.height}cm.")

triangle.describe()