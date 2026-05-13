# Question 1:

# age = int(input("Pleaese Enter Your Age: "))
# if not 0 < age < 121:
#     print("Invalid")
# else:
#     if age > 16:
#         print("Adult")
#     elif age > 12:
#         print("Teen")
#     else:
#         print("Child")

# Question 2

# vowels = ['a','e','i','o','u']
# char = input("Please type a charachter: ").lower()
# if not 96 < ord(char) < 123:
#     print("Invalid")
# else:
#     if char in vowels:
#         print("Vowel")
#     else:
#         print("Consonant")

# Question 3

# age = int(input("Please Enter Your Age: "))
# vip_card = input("Do You Have a VIP Card, Please Answer Yes or No: ").lower()

# if age < 16:
#     print("Rejected")
# elif age == 19 or age == 20 or age == 21:
#     print("You Have Enterd")
# elif vip_card == "yes":
#     print("You Have Enterd")
# else:
#     print("Rejected")

# Question 4
# saved_password = "hello123"

# attempted_password = input("Please Enter The Password: ")

# if len(attempted_password) < 8:
#     print("Password is Too Short")
# elif attempted_password == saved_password:
#     print("Access Granted")
# else:
#     print("Wrong Password")


# Question 5

# x = int(input("Please Enter The x coordinates: "))
# y = int(input("Please Enter The y coordinates: "))

# if not 9 < x < 51 or not 19 < y < 81:
#     print("Outside The Rectangle")
# elif x == 10 or x == 50 or y == 20 or y == 80:
#     print("On The Edge")
# else:
#     print("Inside The Rectangle")


# Question 6
# name = input("Please Enter Your Name: ")
# ano = "Anonymous"
# print(f"Welcome {name or ano}")

# Question 8 (7)

# num1 = int(input("Please Enter a Number: "))
# num2 = int(input("Please Enter a Number: "))
# num3 = int(input("Please Enter a Number: "))

# x = num1 > 0
# y = num2 > 0
# z = num3 > 0

# num_of_positive = x + y + z
# print(num_of_positive)

# Question 10 (8)

# score = int(input("Please Enter Your Score: "))

# grade = "F" if score < 70 else "C" if score < 80 else "B" if score < 90 else "A"
# print(grade)
