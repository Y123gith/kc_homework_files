from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, width, height,side):
        super().__init__(width, height)
        self.side = side

    
    def get_area(self):
       return self.side * self.side

    def get_perimeter(self):
        return 4 * self.side