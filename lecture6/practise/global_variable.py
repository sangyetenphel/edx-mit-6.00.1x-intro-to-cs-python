# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 19:29:33 2019

@author: Sangye Tenphel
"""

def fib(n):
    global counter  # Else we get the error below:
                    # UnboundLocalError: local variable 'counter' referenced before assignment
    counter += 1
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
def fib_using_dict(n, d):
    global counter
    counter += 1
    if n in d:
        return d[n]
    else:
        ans = fib_using_dict(n-1, d) + fib_using_dict(n-2, d)
        d[n] = ans 
        return ans
        
d = {1:1, 2:1}
n = 35

counter = 0
print("")
print(fib(n))
print('classic fib took',counter, 'calls to compute')


counter = 0
print("")
print(fib_using_dict(n,d))
print('fib using dictionary aka memoization',counter, 'calls to compute')
