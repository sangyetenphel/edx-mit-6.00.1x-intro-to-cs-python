# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:11:27 2019

@author: Sangye Tenphel
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    new_tup = ()
    for i in range(len(aTup)):
        if i % 2 == 0:
            new_tup += (aTup[i],)
    
    return new_tup
# =============================================================================
#     
#     new_tup = ()
#     for i in range(0, len(aTup), 2):
#         print(aTup[i])
#         new_tup += (aTup[i],)
#     
#     return new_tup
# 
# =============================================================================
# =============================================================================
# def oddTuples(aTup):
#     '''
#     aTup: a tuple
#     
#     returns: tuple, every other element of aTup. 
#     '''
#     # a placeholder to gather our response
#     rTup = ()
#     index = 0
# 
#     # Idea: Iterate over the elements in aTup, counting by 2
#     #  (every other element) and adding that element to 
#     #  the result
#     while index < len(aTup):
#         rTup += (aTup[index],)
#         index += 2
# 
#     return rTup
# 
# def oddTuples2(aTup):
#     '''
#     Another way to solve the problem.
#  
#     aTup: a tuple
#      
#     returns: tuple, every other element of aTup. 
#     '''
#     # Here is another solution to the problem that uses tuple 
#     #  slicing by 2 to achieve the same result
#     return aTup[::2]
# =============================================================================
        
aTup = ((10, 9, 17, 18))
print(oddTuples(aTup))
        

