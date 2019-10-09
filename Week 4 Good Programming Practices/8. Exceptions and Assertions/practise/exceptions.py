# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 12:20:56 2019

@author: Sangye Tenphel
"""

while True:
    try:
        n = input('Please enter an integer: ')
        n = int(n)
        break
    except ValueError:
        print("Input not an integer; try again")
    print("Correct input of an integer!")