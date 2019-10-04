# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 19:50:53 2019

Write a function called dict_invert that takes in a dictionary with immutable values 
and returns the inverse of the dictionary. The inverse of a dictionary d is another 
dictionary whose keys are the unique dictionary values in d. The value for a key in the 
inverse dictionary is a sorted list (increasing order) of all keys in d 
that have the same value in d.
Here are two examples:
If d = {1:10, 2:20, 3:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3]}
If d = {1:10, 2:20, 3:30, 4:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3, 4]}
If d = {4:True, 2:True, 0:True} then dict_invert(d) returns {True: [0, 2, 4]}

@author: Sangye Tenphel
"""

def dict_invert(d):
    new_d = {}
    for k, v in d.items():
        if v in new_d:
            new_d[v].append(k)
            new_d[v].sort()     # sort the values in ascending order
        else:
            new_d[v] = [k]
    return new_d

# = {1:10, 2:20, 3:30}
d = {1:10, 2:20, 3:30, 5:30, 4:30}
#d = {4:True, 2:True, 0:True}

print(dict_invert(d))
