# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 23:05:43 2019

@author: Sangye Tenphel
"""

def fib(n):
    if n == 0 or n == 1 :
        return 1
    else:
        return fib(n-1) + fib(n-2)