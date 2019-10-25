# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 21:39:01 2019

@author: Sangye Tenphel
"""

def union(L1, L2):
   '''
   L1 & L2 are lists of the same length, n
   '''
   temp = L1[:]
   for e2 in L2:
      flag = False
      for check in temp:
         if e2 == check:
            flag = True
            break
      if not flag:
         temp.append(e2)
   return temp

L1 = [1,2,3]
L2 = [3,4,5]
print(union(L1, L2))