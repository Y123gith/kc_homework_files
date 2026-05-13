# Question 1

# def is_even(a):
#     return a % 2 == 0

# Question 2

# def factorial(n):
#     if n == 0:
#         return 1
#     factor = 1
#     while n > 0:
#         factor = n * factor
#         n -= 1
#     return factor

# Question 3

# def count_vowels(s):
#     vowel_l = ["a","e","i","o","u"]
#     counter = 0
#     for char in s:
#         if char in vowel_l:
#             counter += 1
#     return counter

# Question 4

# def reverse_string(s):
#     s = s[::-1]
#     return s

# Question 5

# def find_max(lst):
#     top_val = lst[0]
#     for value in lst:
#         if value > top_val:
#             top_val = value
#     return top_val

# Question 6

# def celsius_to_fahrenheit(c):
#     return c * (9/5) + 32

# Question 7

# def is_palindrome(s):
#     forward_lst = []
#     backward_lst = []
#     for char in s:
#         forward_lst.append(char)
#     rev_s = s[::-1]
#     for char in rev_s:
#         backward_lst.append(char)
#     return backward_lst == forward_lst

# Question 8

# def only_evens(lst):
#     even_lst = []
#     for value in lst:
#         if value % 2 == 0:
#             even_lst.append(value) 
#     return even_lst

# Question 9

# def is_anagram(s1,s2):
    # s1_lst,s2_lst = [],[]
    # for char in s1:
    #     s1_lst.append(char)
    # for char in s2:
    #     s2_lst.append(char)
    # for char in s1:
    #     if char in s2:
    #         s1_lst.remove(char)
    #         s2_lst.remove(char)
    #     else:
    #         return False
    # return s1_lst == s2_lst

# Question 10

# def word_occurance(sentence):
#     word_dict = {}
#     sentence = sentence.lower()
#     sent_lst = sentence.split(" ")
#     for word in sent_lst:
#         if word in word_dict:
#             word_dict[word] += 1
#         else:
#             word_dict[word] = 1
#     return word_dict

# Question 11

# def calculate_resource_drain(cost,waste_factor):
#     return  cost*waste_factor

# def get_net_resource(cost,waste_factor):
#     result = calculate_resource_drain(cost,waste_factor)
#     return cost - result

# Question 12

# def intercept_length(packet):
#     return len(packet)
# def verify_transmission(packet):
#     return f"Intercepted packet contains {intercept_length(packet)} bytes of data."

# Question 13
# import math

# def convert_to_decibels(signal_strength):
#     return 20 * math.log10(1/signal_strength)
# def is_threat_detected(signal_strength):
#     if convert_to_decibels(signal_strength) > 0.90:
#         return True
#     return False

# Question 14 

# def get_fuel_surcharge(distance):
#     return (distance/10) * 8 * 0.17
# # request is unclear
# def get_hazard_pay(distance):
#     ...
# # request is unclear
# def calculate_mission_cost(distance):
#     ...