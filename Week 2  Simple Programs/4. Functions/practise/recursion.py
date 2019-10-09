# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 22:38:48 2019

@author: Sangye Tenphel
"""

# =============================================================================
# 
# def iterPower(base, exp):
#     '''
#     base: int or float.
#     exp: int >= 0
#  
#     returns: int or float, base^exp
#     '''
#     # Your code here
#     result = 1
#     for i in range(exp):
#         result *= base  
#     return result
# =============================================================================


def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)

