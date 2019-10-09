# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 20:28:28 2019

@author: Sangye Tenphel
"""

from math import *  # import everything from math module to use varables pi and functions like tan
def polysum(n, s):
    """
    n: number of sides
    s: length of each side
    
    returns: sum of area + perimeter squared
    """
    area = (0.25 * n * s**2) / tan(pi/n) # area of regular polygon is: (0.25*n*s^2)/tan(pi/n)
    perimeter = n * s                    # perimeter of a polygon is: length of the boundary of the polygon
    sum =  area + (perimeter**2)
    return round(sum, 4)                 # returns the sum, rounded to 4 decimal places