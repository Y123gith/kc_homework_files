import math

from shape import Shape


class Circle(Shape):
    def __init__(self, id, radius):
        super().__init__(id)
        self.radius = radius
    
    def get_area(self):
        return round((math.pi * self.radius ** 2), 2)
    
    def get_perimeter(self):
        return round(((self.radius * math.pi) * 2), 2)