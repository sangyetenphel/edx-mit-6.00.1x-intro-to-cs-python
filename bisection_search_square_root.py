# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 19:28:12 2019

@author: Sangye Tenphel
"""

x= 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = x
ans = (low + high) / 2.0

while abs(ans**2 - x) >= epsilon:
    print('low =',low,"high =",high, "ans =", ans)
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print("numGuesses", numGuesses)
print("square root of", x, "is close to", ans)
