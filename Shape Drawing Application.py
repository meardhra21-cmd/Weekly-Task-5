from abc import ABC, abstractmethod
import math


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def draw(self):
        print("Drawing a Circle with radius", self.radius)


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def draw(self):
        print("Drawing a Rectangle with length", self.length, "and width", self.width)


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def draw(self):
        print("Drawing a Triangle with base", self.base, "and height", self.height)


circle = Circle(7)
rectangle = Rectangle(10, 5)
triangle = Triangle(6, 4)

print("Circle Area:", circle.area())
circle.draw()

print("\nRectangle Area:", rectangle.area())
rectangle.draw()

print("\nTriangle Area:", triangle.area())
triangle.draw()
