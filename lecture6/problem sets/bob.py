# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 22:12:06 2019

@author: Sangye Tenphel
"""

#s = 'azcbobobegghakl'
s = 'bobobobobobobobobob' # 9
count = 0
for i in range(len(s)-2):
    if s[i:i+3] == 'bob':
        count += 1
print("Number of times bob occurs is:", count)