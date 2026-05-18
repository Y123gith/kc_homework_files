
# 1
# def tuple_sum(tpl):
#     sum = 0
#     for value in tpl:
#         sum += value
#     return sum


# 2
# def max_value(tpl):
#     top_val = tpl[0]
#     for value in tpl:
#         if value > top_val:
#             top_val = value
#     return top_val


# 3
# def count_occurences(tpl,k):
#     counter = 0
#     for number in tpl:
#         if number == k:
#             counter += 1
#     return counter


# 4
# def reverse_tuple(tpl):
#     return tuple(reversed(tpl))


# 5
# def swap_tuple(tpl):
#     temp_lst = []
#     for i in range(0,len(tpl),2):
#         temp_lst.append(tpl[i+1])
#         temp_lst.append(tpl[i])
#     return tuple(temp_lst)


# 6
# def find_min_max(tpl):
#     if len(tpl) == 1:
#         return (tpl[0],tpl[0])
#     min_val = tpl[0]
#     max_val = tpl[0]
#     for value in tpl:
#         if value > max_val:
#             max_val = value
#         elif min_val > value:
#             min_val = value
#     return (min_val, max_val)


# 7 
# def calc_distance(tpl1,tpl2):
#     return (abs(tpl1[1] - tpl1[0]) + abs(tpl2[1] - tpl2[0]))


# 8 
# def combined_sorted_tuple(tpl1,tpl2):
#     return tuple(sorted(tpl1 + tpl2))


# 9
# def count_ocuurences_return_tupled(tpl):
#     temp_lst = []
#     for char in tpl:
#         temp_lst.append((char,tpl.count(char)))
#     return tuple(set(temp_lst))


# 10
def rotate_tuple(tpl,k):
    temp_lst = list(tpl)
    rounds = k % len(temp_lst)
    print(rounds)
    for _ in range(rounds):
        temp_lst.insert(0,temp_lst.pop())
    return tuple(temp_lst)

print(rotate_tuple((1, 2, 3, 4, 5), 7))