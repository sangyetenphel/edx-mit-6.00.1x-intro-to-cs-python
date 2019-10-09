# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 20:45:00 2019

@author: Sangye Tenphel
"""

def avg(grades):
    assert not len(grades) == 0, 'no grades data'
    return sum(grades)/len(grades)

print(avg([]))
