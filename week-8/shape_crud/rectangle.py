from shape import Shape


class Rectangle(Shape):
    def __init__(self, id, width, height):
        super().__init__(id)
        self.width = width
        self.height = height
    
    def get_area(self):
        return round((self.width * self.height), 2)
    
    def get_perimeter(self):
        return round((self.width * 2 +  self.height * 2), 2)