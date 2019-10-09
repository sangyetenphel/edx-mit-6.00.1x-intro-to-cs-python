# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 10:45:03 2019

@author: Sangye Tenphel
"""
cube = 29
epsilon = 0.01 # reduce epsilon for more accurate answer
guess = 0.0
step = 0.0001  # increase step to get faster program
num_guesses = 0

while (cube - guess**3) >= epsilon:
    guess += step
    num_guesses += 1
print("num_guesses =", num_guesses) # to see how many guesses it generarted
   
if (cube - guess**3) >= epsilon:
    print("cube root not found")
else:
    print("cube root of", cube, "is close to", guess)