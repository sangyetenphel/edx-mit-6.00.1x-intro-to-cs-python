# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 17:23:39 2019

@author: Sangye Tenphel
"""
# =============================================================================
# # produces an ‘iterable’, so need to walk down it
# for ele in map(abs, [-3, -9.0]):
#     print(ele)
# =============================================================================

# general form – an n-ary function and n collections of arguments 
L1 = [9, 1, 1]
L2 = [6, 1, 9]

for ele in map(min, L1, L2):
    print(ele)