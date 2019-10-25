# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 13:02:00 2019

@author: Sangye Tenphel
"""
def selSort(L):
    prefix = 0
    while prefix < len(L):
        for i in range(prefix, len(L)):
            if L[i] < L[prefix]:
                L[prefix], L[i] = L[i], L[prefix]
        prefix += 1
    return L


L = [1,5,6,0,2,4,0,9,6,0]