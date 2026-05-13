# Question 1
# for i in range(1,11):
#     if i % 2 == 0:
#         continue
#     if i == 7:
#         break
#     print(i)


# Question 2
# the_passwd = 25847
# while True:
#     passwd = int(input("Please Enter Your Password: "))
#     if passwd == the_passwd:
#         print("Welcome!")
#         break
#     print("Try Again")

# Question 3.1
# products = []
# while True:
#     product = input("Please Enter the Product Name: ")
#     if product == "done":
#         break
#     products.append(product)
# for item in products:
#     print(item)

# Question 3.2

# for i in range(1,4):
#     for j in range(1,4):
#         if j == 2:
#             break
#         print(f"{i},{j}", end=" ")
#     print("")

# Question 4
# number_of_vowels = 0
# vowels = ["a","e","i","o","u"]
# word = input("Please Enter a Word: ")
# for char in word:
#     if char in vowels:
#         number_of_vowels += 1
# print(number_of_vowels)

# Question 5 

# for i in range(1,6):
#     for j in range(1,6):
#         print(f"{i}x{j} = {i*j} ", end="")
#     print("")

# Question 6

# word = input("Please Enter a Word: ")
# i = len(word)-1
# for _ in word:
#     print(word[i],end="")
#     i -= 1

# Question 7
# num = int(input("Please Enter an int: "))
# counter = 0
# while num > 1:
#     num = num // 2
#     counter = counter + 1
# print(counter)

# Question 8

# word = input("Please Enter a Word: ")
# for char in word:
#     print(char*2, end="")

# Question 9

# top_num = 0
# while True:
#     num = int(input("Please Enter a positive int: "))
#     if num == 0:
#         break
#     if num > top_num:
#         top_num = num
# print(top_num)


# Question 10

# text = input("Please enter a string: ")
# test_key = True
# for char in text:
#     if not 47<ord(char)<58 and not 64<ord(char)<91 and not 96<ord(char)<123:
#         print("False")
#         test_key = False
#         break
# if test_key:
#     print("True")

# Question 11

# num = int(input("Please Enter a Number: "))
# num_lst = []
# rever_num = 0
# while num > 9:
#     num_lst.append(num % 10)
#     num = num // 10
# num_lst.append(num)
# for i,number in enumerate(num_lst):
#     rever_num = rever_num + number*(10**(len(num_lst)-i-1))
# print(rever_num)