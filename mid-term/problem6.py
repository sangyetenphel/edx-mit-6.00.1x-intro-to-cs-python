# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 21:42:06 2019

Write a Python function that takes in two lists and calculates whether they are permutations of each other. 
The lists can contain both integers and strings. We define a permutation as follows:
- the lists have the same number of elements
- list elements appear the same number of times in both lists
If the lists are not permutations of each other, the function returns False. 
If they are permutations of each other, the function returns a tuple consisting of the following elements:
- the element occuring the most times
- how many times that element occurs
- the type of the element that occurs the most times
If both lists are empty return the tuple (None, None, None). 
If more than one element occurs the most number of times, you can return any of them.
For example,
if L1 = ['a', 'a', 'b'] and L2 = ['a', 'b'] then is_list_permutation returns False
if L1 = [1, 'b', 1, 'c', 'c', 1] and L2 = ['c', 1, 'b', 1, 1, 'c'] then is_list_permutation returns (1, 3, <class 'int'>) because the integer 1 occurs the most, 3 times, and the type of 1 is an integer (note that the third element in the tuple is not a string).

@author: Sangye Tenphel
"""

def is_list_permutation(l1, l2):
    if l1 == [] and l2 == []:
        return (None, None, None)
    
    if len(l1) != len(l2):
        return False
    
    matching_ele = {}
    for ele in l1:
        if ele in l2:
            if ele in matching_ele:
                matching_ele[ele] += 1
            else:
                matching_ele[ele] = 1
            l2.remove(ele)
    
    #most_occuring = 0         
    frequency = 0
    for k, v in matching_ele.items():
        if v > frequency:
            frequency = v
            most_occuring = k
            
    return (most_occuring, frequency, type(most_occuring))

# =============================================================================
# l1 = [1, 'b', 1, 'c', 'c', 1]
# l2 = ['c', 1, 'b', 1, 1, 'c']
# =============================================================================
# =============================================================================
# l1 = []
# l2 = []
# =============================================================================
l1 = ['a', 'a', 'b']
l2 = ['a', 'b'] 
print(is_list_permutation(l1, l2))