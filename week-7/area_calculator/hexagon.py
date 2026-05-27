from math import sqrt
from calculater import Shape

class Hexagon(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return (3 * sqrt(3) * self.side ** 2) / 2
    
    def get_perameter(self):
        return 6 * self.side
    
    def __str__(self):
        return f" Shape: {type(self).__name__}\n Area: {self.get_area()}\n Perimeter: {self.get_perameter()}"