from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, id):
        self.id = id
        self.shape_type = type(self).__name__
        
    def __setattr__(self, name, value):
        if name in ('shape_type', 'id'):
            super().__setattr__(name, value)
            return

        if not isinstance(value, (int, float)):
            raise TypeError(f"Error: Value for {name} must be a number")
        if value <= 0:
            raise ValueError(f"Error: Value for {name} must be greater than zero")
        super().__setattr__(name, value)
        
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    def __repr__(self):
        return f"Shape: {type(self).__name__}, size: {self.get_area()}, perimeter: {self.get_perimeter()} | Param: {self.__dict__}"
            

    def __str__(self):
        return f"[{self.id}] Shape: {type(self).__name__}, size: {self.get_area()}, perimeter: {self.get_perimeter()}"
    
    def __eq__(self, other):
        if isinstance(other, Shape):
            return self.get_area() == other.get_area()
        return False
    
    def __lt__(self, other):
        if isinstance(other, Shape):
            return self.get_area() < other.get_area()
        raise TypeError("Can only compare between Shapes")
    
    def __gt__(self, other):
        if isinstance(other, Shape):
            return self.get_area() > other.get_area()
        raise TypeError("Can only compare between Shapes")
    
    def __add__(self, other):
        if isinstance(other, Shape):
            return self.get_area() + other.get_area()
        raise TypeError("Can only add Shapes together")
    
    def to_dict(self):
        return self.__dict__
    
    @classmethod
    def recreate_shape_from_dict(cls, shape: dict) -> 'Shape':
        def get_all_subclasses(c):
            subs = c.__subclasses__()
            for sub in c.__subclasses__():
                subs.extend(get_all_subclasses(sub))
            return subs
        
        shape_data = shape.copy()
        shape_type = shape_data.pop('shape_type', None)

        if not shape_type:
            raise ValueError('Error: No shape_type found')
        
        subclass = {sub.__name__: sub for sub in get_all_subclasses(cls)}
        target_class = subclass.get(shape_type)

        if not target_class:
            raise ValueError('Error: not a shape instance')
        
        return target_class(**shape_data)