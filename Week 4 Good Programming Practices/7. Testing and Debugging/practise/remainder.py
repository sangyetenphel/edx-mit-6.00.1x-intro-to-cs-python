# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 11:41:53 2019

@author: Sangye Tenphel
"""

def rem(x, a):
    """
    x: a non-negative integer argument
    a: a postive integer argument
    
    returns: integer, the remainder when x is divided by a
    """
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        return rem(x-a, a)
        
print(rem(7, 5))
