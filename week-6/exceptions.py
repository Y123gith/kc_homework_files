
# 1
# def safe_int(s):
#     try:
#         s = int(s)
#     except ValueError:
#         return None
#     else:
#         return s
    

# 2
# def safe_divide(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         return "undefined"


# 3 
# def read_first_line(path):
#     try:
#         with open(path,"r") as f:
#             return f.readlines(1)
        
#     except FileNotFoundError:
#         return None


# 4
# def get_value(d, key):
#     try:
#         return d[key]
#     except KeyError:
#         return "missing"


# 5
# def parse_ints(values):
#     int_values_lst = []
#     for value in values:
#         try:
#             value = int(value)
#         except ValueError:
#             pass
#         else:
#             int_values_lst.append(value)
#     return int_values_lst


# 6
# def set_age(age):
#     if 0 < age < 150:
#         return age
#     else:
#         raise ValueError


# 7
# class InsufficientFundsError(Exception):
#     ...


# def withdraw(balance, amount):
#     if balance > amount:
#         return balance - amount
#     else:
#         raise InsufficientFundsError


# 8
# def retry(func, n):
#     for i in range(n):
#         try:
#             result = func()
#         except Exception:
#             pass
#         else:
#             return result
#     raise 


# 9
# def count_errors(funcs):
#     counter = 0
#     for function in funcs:
#         try:
#             function()
#         except Exception:
#             counter += 1
#     return counter


# 10
# def load_config(path):
#     with open(path, "r") as f:
#         try:
#             return int(f.readline().strip())
#         except Exception as e:
#            raise RuntimeError("failed to loadconfig") e


    

            

