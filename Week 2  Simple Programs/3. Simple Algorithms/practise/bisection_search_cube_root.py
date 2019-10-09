# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 21:33:57 2019

@author: Sangye Tenphel
"""

x = -27
abs_x = abs(x)
epsilon = 0.01
low = 0
high = abs_x
ans = (high + low) / 2
numGuesses = 0

while abs(abs_x - ans**3) >= epsilon:
    if ans**3 > abs_x:
        high = ans
    else:
        low = ans
    ans = (high + low) / 2
    numGuesses += 1
print("numGuesses", numGuesses)

if x < 0:
    ans = - ans
print("The cube root of", x, "is close to", ans)