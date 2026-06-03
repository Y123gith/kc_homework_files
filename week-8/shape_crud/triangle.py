import math
from shape import Shape

class Triangle(Shape):
    def __init__(self, id, side_a, side_b, side_c):
        super().__init__(id)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

        illegal_conditions = [
            side_a + side_b <= side_c,
            side_a + side_c <= side_b,
            side_b + side_c <= side_a
        ]

        if any(illegal_conditions):
            raise ValueError("not a ligle triangle")
        
    def get_perimeter(self):
        return round((self.side_a + self.side_b + self.side_c), 2)

    def get_area(self):
        s = self.get_perimeter() / 2
        area = math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))
        return round(area, 2)