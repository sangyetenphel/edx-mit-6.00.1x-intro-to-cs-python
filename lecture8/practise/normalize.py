# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 22:08:22 2019

@author: Sangye Tenphel
"""

def normalize(numbers):
    '''
    numbers: list of positive numbers
    returns: list, numbers that are fraction of the max ele in the list
    '''
    max_number = max(numbers)
    assert max_number != 0, 'why? why? zero?' # pre condition
    #assert(max_number != 0), 'Cannot divide by 0' 
    for i in range(len(numbers)):
        numbers[i] /= float(max_number)
        assert(0.0 >= numbers[i] <= 1.0), 'output not bewtween 0 and 1' # post condition
    return numbers

print(normalize([0,0,0]))