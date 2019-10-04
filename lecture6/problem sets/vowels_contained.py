# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 22:06:33 2019

@author: Sangye Tenphel
"""

s = 'azcbobobegghakl'

vowels = 'aeioiu'
count = 0
for char in s:
    if char in vowels:
        count += 1
print('Number of vowels:', count)