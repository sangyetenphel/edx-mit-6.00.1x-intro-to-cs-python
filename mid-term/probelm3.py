# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 19:02:19 

Write a function that satisfies the following docstring.
For example, if
largest_odd_times([2,2,4,4]) returns None
largest_odd_times([3,9,5,3,5,3]) returns 9

@author: Sangye Tenphel
"""

def largest_odd_times(l):
    """
    l: list of positive inegers
    returns: integer, largest odd integer in the list
    """
    
    odds = []
    for num in l:
        if num % 2 != 0:
            odds.append(num)
            
    if odds == []:
        return None
    else:
        return max(odds)

    
large = largest_odd_times([2,2,4,4])
print(large)
print(type(large))

largest = largest_odd_times([3,9,5,3,5,3])
print(largest)
print(type(largest))
