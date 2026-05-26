## 1
# class Student:
#     def __init__(self, name):
#         self._name = name

#     @property
#     def name(self):
#         return self._name

# # 2 
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     @property
#     def area(self):
#         return self.width * self.height
    
# rec = Rectangle(2,3)
# rec.area = 7
        

# # 3
# class Thermometer:
#     def __init__(self,celsius):
#         self._celsius = celsius
    
#     @property
#     def celsius(self):
#         return self._celsius

#     @celsius.setter
#     def celsius(self,number):
#         if int(number) < -273.15:
#             raise ValueError
#         self._celsius = number


# # 4
# class BankAccount:
#     def __init__(self,balance):
#         self._balance = balance

#     @property
#     def balance(self):
#         return self._balance
    
#     def deposit(self,amount):
#         self._balance += amount

#     def withdraw(self,amount):
#         if amount > self._balance:
#             raise ValueError("not enough money in account")
#         self._balance -= amount


# # 5
# class Person:
#     def __init__(self,first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name

#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"


# # 6
# class Temperature:
#     def __init__(self, celsius):
#         self._celsius = celsius

#     @property
#     def celsius(self):
#         return (self._celsius * 1.8) + 32
    
#     @celsius.setter
#     def celsius(self,fahrenheit):
#         self._celsius = (fahrenheit - 32)/1.8


# # 7
# class Calculator:
#     @staticmethod
#     def is_even(n):
#         return n % 2 == 0


# # 8 
# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

#     @classmethod
#     def from_tuple(cls,pair):
#         x,y = pair
#         return cls(x,y)
        

# # 9 
# class User:
#     counter = 0

#     def __init__(self):
#         User.counter += 1
#     @classmethod
#     def how_many(cls):
#         return cls.counter


# # 10
# class Product:
#     def __init__(self, name, price):
#         self._name = name
#         self._price = price

#     @property
#     def name(self):
#         return self._name
    
#     @property
#     def price(self):
#         return self._price
    
#     @price.setter
#     def price(self,new_price):
#         if new_price >= 0:
#             self._price = new_price
#         else:
#             print("Cannot set a negative price")