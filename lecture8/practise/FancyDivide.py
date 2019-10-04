# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 18:34:34 2019

@author: Sangye Tenphel
"""

def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError: # handling this specific error
        return 0              # return 0 for this exception

print(fancy_divide([0, 2, 4], 0))