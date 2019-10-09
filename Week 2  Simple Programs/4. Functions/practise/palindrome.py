# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 11:55:02 2019

@author: Sangye Tenphel
"""
def clean_str(string):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    new_string = ''
    for char in string.lower():
        if char in alpha:
            new_string += char
    return new_string
    
    
def palindrome(string):
    if len(string) == 0 or len(string) == 1:
        return True
    else:
        return string[0] == string[-1] and palindrome(string[1:-1])

palindrome(clean_str("Ava"))        