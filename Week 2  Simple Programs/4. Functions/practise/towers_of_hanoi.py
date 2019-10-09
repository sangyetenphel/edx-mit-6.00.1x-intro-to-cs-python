# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 23:09:19 2019

@author: Sangye Tenphel

Based from this link: https://www.youtube.com/watch?v=5_6nsViVM00
Not from the Edx MIT 6.00.1x course

"""

def Towers(n, beg, aux, end):
    if n == 1:
        print("move from", beg, "to", end)
    else:
        Towers(n-1, beg, end, aux)
        Towers(1, beg, aux, end)
        Towers(n-1, aux, beg, end)
        
Towers(3, "A", "B", "C")