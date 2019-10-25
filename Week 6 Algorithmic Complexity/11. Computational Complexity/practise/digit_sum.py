# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 19:13:28 2019

@author: Sangye Tenphel
"""
# Example of O(log n)
def sumOfDigits(num):
    '''Assume num is integer >= 0 '''
    s = str(num)
    answer = 0
    for n in s:
        answer += int(n)
    return answer

print(sumOfDigits(123))

