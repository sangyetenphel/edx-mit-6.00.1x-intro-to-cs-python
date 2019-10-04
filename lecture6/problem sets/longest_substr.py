# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 22:21:31 2019

@author: Sangye Tenphel
"""

#s = 'azcbobobegghakl'
#s = 'abcbcd'
s = 'zlicqkoddz'  #ddz


current = s[0]
longest = s[0]

for char in s[1:]:
    if char >= current[-1]:
        current += char
    else:
        current = char
        
    if len(current) > len(longest):
        longest = current

print("Longest substring in alphabetical order is:", longest)
    
# =============================================================================
# longest = ''
# longest_substr = ''
# 
# for i in range(len(s)-1):
#     longest = s[i]
#     while s[i] <= s[i+1]:
#         longest += s[i+1]
#         i += 1
#         if i == (len(s)-1):
#             break
#     
#     if len(longest) >= len(longest_substr):
#         longest_substr = longest
# 
# print("Longest substring in alphabetical order is:", longest_substr)
# =============================================================================
