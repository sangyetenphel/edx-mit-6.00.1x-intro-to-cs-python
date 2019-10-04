# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 13:05:32 2019

@author: Sangye Tenphel
"""

def fact(n):
    '''
    n: integer, n >= 0.
    '''
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
    
print(fact(4))