import math

from shape import Shape


class Hexagon(Shape):
    def __init__(self, id, side):
        super().__init__(id)
        self.side = side

    def get_area(self):
        return round(((3 * math.sqrt(3) * self.side ** 2) /2), 2)
    
    def get_perimeter(self):
        return round((self.side * 6), 2)