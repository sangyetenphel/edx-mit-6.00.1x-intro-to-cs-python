# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 11:47:39 2019

@author: Sangye Tenphel
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a > b:
        gcd = b
    else:
        gcd = a
    
    while True:
        if a % gcd == 0 and b % gcd == 0:
            return gcd 
        gcd -= 1 
        
        
        
# =============================================================================
# # MIT version
# 
# def gcdIter(a, b):
#     '''
#     a, b: positive integers
#     
#     returns: a positive integer, the greatest common divisor of a & b.
#     '''
#     testValue = min(a, b)
# 
#     # Keep looping until testValue divides both a & b evenly
#     while a % testValue != 0 or b % testValue != 0:
#         testValue -= 1
# 
#     return testValue
# =============================================================================



