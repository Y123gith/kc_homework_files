# 1
# class Dog:
#     def __init__(self,name):
#         self.name = name
    

#     def bark(self):
#         return f"{self.name} says woof"


# 2 
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

    
#     def area(self):
#         return self.width * self.height
        

# # 3
# class Counter:
#     def __init__(self,number=0):
#         self.number = number
    
#     def increment(self):
#         self.number += 1

#     def value(self):
#         return self.number
    

# # 4
# class Point:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def __str__(self):
#         return f"({self.a},{self.b})"
    

# # # 5
# class BankAccount:
#     def __init__(self, balance=0):
#         self.balance = balance
    
#     def deposit(self,amount):
#         self.balance += amount
    
#     def withdraw(self,amount):
#         if amount < self.balance:
#             self.balance -= amount       


# # 6
# class Temprature:
#     def __init__(self, celsious):
#         self.celsious = celsious

#     def to_fahrenheit(self):
#         fahrenheit = (1.8 * self.celsious) + 32
#         return fahrenheit


# # 7
# class Student:
#     school = "Kodcode"
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return f"school:{self.school}, name:{self.name} "
    
# s1 = Student("Y")
# s2 = Student("D")
# print(s1,s2)


# 8 
# class Player:
#     counter = 0
#     def __init__(self):
#         self.counter += 1


# 9 
# class Money:

#     def __init__(self, amount):
#         self.amount = amount
    
#     def is_more_than(self,other):
#         return self.amount > other.amount 
    

# class Playlist:
#     def __init__(self,song_titles):
#         self.song_titles = song_titles 
    
#     def add(self,song_t):
#         self.song_titles.append(song_t)
    
#     def remove(self,song_t):
#         self.song_titles.pop(song_t)
        
#     def count(self):
#         return len(self.song_titles)
        
#     def __str__(self):
#         return f"{self.song_titles}"
        
