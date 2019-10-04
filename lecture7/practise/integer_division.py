# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 22:11:34 2019

@author: Sangye Tenphel
"""

def integerDivision(x, a):
    """
    x: a non-negative integer argument
    b: a positive integer argument
    
    returns: integer, the integer division of x divided by a.
    """
    count = 0
    while x >= a:
        count += 1
        x -= a
    return count

print(integerDivision(5, 3))