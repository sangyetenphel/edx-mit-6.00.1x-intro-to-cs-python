# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 20:41:59 2019

Write a function called general_poly, that meets the specifications below. 
For example, general_poly([1, 2, 3, 4])(10) should evaluate to 1234 
because 1*(10**3) + 2*(10**2) + 3*(10**1) + 4*(10**0).

@author: Sangye Tenphel
"""

def general_poly(l, n):
    result = 0
    power = len(l) - 1 
    for num in l:
        result += num * (n**power)
        power -= 1 
    return result

print(general_poly([1, 2, 3, 4], 10))