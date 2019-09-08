# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 17:59:25 2019

@author: Sangye Tenphel
"""

x = -9
guess = x / 2
epsilon = 0.01
numGuesses = 0 

while abs(guess**2 - x) > epsilon:
    guess = guess - ((guess**2 - x)/(2*guess))
    numGuesses += 1
    
print("numGuesses:", numGuesses)
print("The square root of", x, "is about", guess)