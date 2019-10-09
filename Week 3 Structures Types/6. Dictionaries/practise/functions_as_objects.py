# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 16:58:09 2019

@author: Sangye Tenphel
"""
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
    
L = [1, 2.0, -3.5, -4]
#applyToEach(L, abs)


def applyFuns(L, e):
    for f in L:
        print(f(e))
    
applyFuns([abs, int], -4.4)