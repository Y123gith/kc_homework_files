from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, id, side):
        super().__init__(id, side, side)