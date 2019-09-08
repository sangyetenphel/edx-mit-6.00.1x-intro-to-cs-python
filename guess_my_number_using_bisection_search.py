# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 22:34:07 2019

@author: Sangye Tenphel
"""

low = 0
high = 100
print("Please think of a number between 0 and 100!")
while True:
    mid = int((low + high) / 2)
    print("Is your secret number " + str(mid) + "?")
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ").lower()
    if ans == 'h':
        high = mid
    elif ans == 'l':
        low = mid
    elif ans == 'c':
        print("Game over. Your secret number was:", mid)
        break
    else:
        print("Sorry, I did not understand your input.")
