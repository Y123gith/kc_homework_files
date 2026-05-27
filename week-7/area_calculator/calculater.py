
class Shape():
  
    def get_area():
        ...
    
    def get_perimeter():
        ...

    def __str__(self):
        return f" Shape: {type(self).__name__}\n Area: {self.get_area()}\n Perimeter: {self.get_perimeter()}"
    
    def __repr__(self):
        return f"Type:{type(self)}"

    def __setattr__(self, name, value):
        if not isinstance(value,int|float) or not value > 0:
            raise ValueError("values must be numbers")
        super().__setattr__(name,value)
