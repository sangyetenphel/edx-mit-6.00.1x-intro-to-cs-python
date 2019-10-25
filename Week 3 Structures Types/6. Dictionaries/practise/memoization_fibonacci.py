# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 13:01:39 2019

@author: Sangye Tenphel
"""

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
def fib_using_dict(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_using_dict(n-1, d) + fib_using_dict(n-2, d)
        d[n] = ans 
        return ans
        
d = {1:1, 2:1}
n = 35
print("")
print('classic fib')
print(fib(n))
print("")
print('fib using dictionary aka memoization')
print(fib_using_dict(n,d))
