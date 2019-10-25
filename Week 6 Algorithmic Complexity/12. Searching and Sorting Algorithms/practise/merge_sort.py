# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 22:49:37 2019

@author: Sangye Tenphel
"""

def merge(left, right):
    result = []
    #i = 0 
    #j = 0
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
# =============================================================================
#     if i < len(left):
#         result += left[i:]
#     elif j < len(right):
#         result += right[j:]
# =============================================================================
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1 
        
    return result

def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        mid = len(L) // 2
        left = merge_sort(L[:mid])
        right = merge_sort(L[mid:])
        return merge(left, right)
    
L = [1,4,0,6]
print(merge_sort(L))
        
        