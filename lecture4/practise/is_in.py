# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 12:30:39 2019

@author: Sangye Tenphel
"""

# =============================================================================
# def isIn(char, aStr):
#     def sort(aStr): 
#         new_string = ''
#         for char in sorted(aStr):
#             new_string += char
#         return new_string
#     
#     def is_in(aStr):
#         mid = aStr[len(aStr) // 2]
#         mid_idx = aStr.index(mid)
#         if len(aStr) <= 1 and mid == char:
#             return True
#         elif len(aStr) <= 1 and mid != char:
#             return False
#         else:
#             if char < mid:
#                 return is_in(aStr[0:mid_idx])
#             else:
#                 return is_in(aStr[mid_idx+1:])
#                 
#     return is_in(sort(aStr))
# 
# 
# print(isIn('a','apple'))
# =============================================================================

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if aStr == '':          # Base case: If aStr is empty, we did not find the char.
        return False
        
    if len(aStr) == 1:      # Base case: if aStr is of length 1, just see if the chars are equal
        return aStr == char
    
    midIndex = len(aStr) // 2
    midChar = aStr[midIndex]
    if char == midChar:     # See if the character in the middle of aStr equals the test character 
        return True
    elif char < midChar:    # Recursive case: If the test character is smaller than the middle character, recursively search on the first half of aStr
        return isIn(char, aStr[:midIndex])
    else:                   # Otherwise the test character is larger than the middle character, so recursively search on the last half of aStr
        return isIn(char, aStr[midIndex + 1:])
        
        
print(isIn('q', 'abcfgijmppppqsssyzz'))    # True

