# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 22:36:45 2019

@author: Sangye Tenphel
"""

def genSubsets(L):
    if len(L) == 0:
        return [[]]  # list of empty list 
    smaller = genSubsets(L[:-1]) # all subsets without last element
    print("smaller:", smaller)
    
    extra = L[-1:]  # create a list of just last element 
    new = []
    for small in smaller:
        print('small:', small,"extra:", extra)
        print('small + extra:', small + extra)
        new.append(small + extra) # for all smaller solutions, add one with last element 
        print("new:", new)
        print('----------------')
    return smaller + new # combine those with last element and those without

L = [1, 2]
subsets = genSubsets(L)
print(subsets)