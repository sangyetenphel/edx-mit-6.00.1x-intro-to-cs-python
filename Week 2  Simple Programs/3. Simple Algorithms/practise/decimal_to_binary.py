# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 14:03:11 2019

@author: Sangye Tenphel
"""

num = -3

if num < 0:       # this block of if/else statement is cool to solve for negative integer
    isNeg = True
    num = abs(num)
else:
    isNeg = False

result = ''  
while num > 0:
    result = str(num % 2) + result # tricky part for me 
    num = num // 2
    
if isNeg:
    result = '-' + result
    