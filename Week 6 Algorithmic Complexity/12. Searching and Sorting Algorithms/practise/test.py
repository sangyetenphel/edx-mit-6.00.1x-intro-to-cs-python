# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:08:13 2019

@author: Sangye Tenphel
"""

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
 
def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False

for i in (0,1,2,3,4,5):
    L = [1,2,3]
    print(i, ":", search(L, i), ",", newsearch(L, i))

