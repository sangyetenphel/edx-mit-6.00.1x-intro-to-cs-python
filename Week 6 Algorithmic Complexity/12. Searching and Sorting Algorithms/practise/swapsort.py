# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:16:30 2019

@author: Sangye Tenphel
"""

def swapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)
    
    
L = [9,1,7,4,5,5,4,9,3,6]
print(swapSort(L))