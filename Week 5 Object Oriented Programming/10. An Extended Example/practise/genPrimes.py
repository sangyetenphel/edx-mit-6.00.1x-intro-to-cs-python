# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 22:39:24 2019

@author: Sangye Tenphel
"""

def genPrimes():
    '''returns sequence of prime numbers on successive calls'''
    primes = [2]
    x = 3
    while True:
        for p in primes:
            if (x % p) == 0:
                break
        else:   # belongs to the for loop and runs if no break was occured 
            yield primes[-1]
            primes.append(x)
        x += 1
            
        