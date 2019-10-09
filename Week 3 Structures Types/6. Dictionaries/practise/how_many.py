# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 10:13:43 2019

@author: Sangye Tenphel
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

# =============================================================================
# animals['d'] = ['donkey']
# animals['d'].append('dog')
# animals['d'].append('dingo')
# =============================================================================

def how_many(aDict):
    values = aDict.values()
    count = 0
    for value in values:
        count += len(value)
    return count

# =============================================================================
# def how_many(aDict):
#     '''
#     aDict: A dictionary, where all the values are lists.
# 
#     returns: int, how many individual values are in the dictionary.
#     '''
#     result = 0
#     for value in aDict.values():
#         # Since all the values of aDict are lists, aDict.values() will 
#         #  be a list of lists
#         result += len(value)
#     return result
# 
# def how_many(aDict):
#     '''
#     Another way to solve the problem.
# 
#     aDict: A dictionary, where all the values are lists.
# 
#     returns: int, how many individual values are in the dictionary.
#     '''
#     result = 0
#     for key in aDict.keys():
#         result += len(aDict[key])
#     return result
# =============================================================================



def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    freq = []
    values = aDict.values()
    for value in values:
        freq.append(len(value))
        
    for k,v in aDict.items():
        if len(v) == max(freq):
            return k

# =============================================================================
# def biggest(aDict):
#     '''
#     aDict: A dictionary, where all the values are lists.
# 
#     returns: The key with the largest number of values associated with it
#     '''
#     result = None
#     biggestValue = 0
#     for key in aDict.keys():
#         if len(aDict[key]) >= biggestValue:
#             result = key
#             biggestValue = len(aDict[key])
#     return result
# =============================================================================
        
    
