# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 11:55:18 2019

@author: Sangye Tenphel
"""
def bubble_sort(l):  # Overall Complexity of O(n**2) i.e. O(n*n)
    flag = False
    while not flag:  # O(n)
        flag = True
        for i in range(1, len(l)):   #O(n)
            if l[i-1] > l[i]:
                flag = False
                temp = l[i-1]
                l[i-1] = l[i]
                l[i] = temp
    return l           

l = [9,1,7,4,5,5,4,9,3,6]
print(bubble_sort(l))
