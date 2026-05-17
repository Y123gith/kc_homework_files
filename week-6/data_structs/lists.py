
# 1
# def sum_list(lst):
#     sum = 0
#     for value in lst:
#         sum += value
#     return sum 


# 2
# def max_value(lst):
#     max = lst[0]
#     for value in lst:
#         if value > max:
#            max = value
#     return max


# 3
# def count_ocuurences(lst,number):
#     counter = 0
#     for value in lst:
#         if number == value:
#            counter += 1
#     return counter


# 4
# import copy
# def reverse_lst(lst):
#     reversed_lst = []
#     temp_lst = lst.copy()
#     for _ in temp_lst:
#         reversed_lst.append(temp_lst.pop())
#     return reversed_lst


# 5
# def remove_duplicates(lst):
#     no_duplicates_lst = []
#     for value in lst:
#         if value not in no_duplicates_lst :
#             no_duplicates_lst.append(value)
#     return no_duplicates_lst


# 6
# def second_to_max(lst):
#     copy_lst = lst[:]
#     absolute_max = max(lst)
#     while True:
#         if absolute_max in copy_lst:
#             copy_lst.remove(absolute_max)
#         else:
#             break
#     return max(copy_lst)


# 7
# def two_into_one_sorted(lst1,lst2):
#     merged_lst = []
#     merged_lst.extend(lst2 + lst1)
#     return sorted(merged_lst)


# 8 
# def rotate_lst(lst,k):
#     rounds = len(lst) % k
#     for _ in range(rounds + 1):
#         lst.insert(0,lst.pop())
#     return lst