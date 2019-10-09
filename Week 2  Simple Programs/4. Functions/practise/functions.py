# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 22:36:33 2019

@author: Sangye Tenphel
"""
# =============================================================================
# 
# def func_a():
#     print('inside func_a')
# def func_b(y):
#     print('inside func_b')
#     return y
# def func_c(z):
#     print('inside func_c')
#     return z()
# print(func_a())       # inside func_a, none
# print(5 + func_b(2))  # inside_func_b, 7
# print(func_c(func_a)) # inside_func_c, inside func_a, none
# =============================================================================


# =============================================================================
# def f(y):
#     x = 1
#     x += 1
#     print(x)
#     
# x = 5
# f(x)     # 2
# print(x) # 5
# =============================================================================

# =============================================================================
# def g(y):
#     print(x)
#     print(x + 1)
# 
# x = 5
# g(x)      # 5, 6
# print(x)  # 5
# =============================================================================


def h(y):
    x = x + 1
    
x = 5
h(x)     # UnboundLocalError: local variable 'x' referenced before assignment
print(x) # becoz inside a function, cannot modify a variable defined outside

