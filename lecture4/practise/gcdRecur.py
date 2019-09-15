# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 21:36:09 2019

@author: Sangye Tenphel
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)