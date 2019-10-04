# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 13:22:56 2019

Write a Python function that takes in a string and prints out a version of this string 
that does not contain any vowels, according to the specification below. 
Vowels are uppercase and lowercase 'a', 'e', 'i', 'o', 'u'.
For example, if s = "This is great!" then print_without_vowels will print Ths s grt!. 
If s = "a" then print_without_vowels will print the empty string .

@author: Sangye Tenphel
"""

def print_without_vowels(s):
    new_str = ''
    vowels = 'aeiouAEIOU'
    for char in s:
        if char not in vowels:
            new_str += char
    return new_str

print(print_without_vowels('This is great!'))