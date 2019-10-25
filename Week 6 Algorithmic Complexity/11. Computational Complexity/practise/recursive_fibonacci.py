# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 19:38:12 2019

@author: Sangye Tenphel
"""

def fib(n):  # Example of O(2**n) i.e. Exponential Complexity
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# =============================================================================
# def fib(n):   # Using Memoization we reduce the complexity to O(n) i.e.Linear Complexity
#     def fib_memo(n, m):
#         if n in m:
#             return m[n]
#         else:
#             ans = fib_memo(n-1, m) + fib_memo(n-2, m)
#             m[n] = ans
#             return ans
#     
#     m = {0: 0, 1: 1}
#     return fib_memo(n, m)
# 
# =============================================================================
print(fib(36))