# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 21:24:54 2019

@author: Sangye Tenphel
"""

# =============================================================================
# def genTest():
#     yield 1
#     yield 2
# =============================================================================


def genFib():
    fibn_1 = 1  #fib(n-1)
    fibn_2 = 0  #fib(n-2)
    while True:
        # fib(n) = fib(n-1) + fib(n-2)
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next
        