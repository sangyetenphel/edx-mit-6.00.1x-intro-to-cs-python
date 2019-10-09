# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 20:25:09 2019

@author: Sangye Tenphel
"""

# =============================================================================
# class intSet(object):
#     def __init__(self):
#         self.vals = []
#         
#     def insert(self, ele):
#         if ele not in self.vals:
#             self.vals.append(ele)
#         
#     def member(self, ele):
#         return ele in self.vals
#     
#     def remove(self, ele):
#         try:
#             self.vals.remove(ele)
#         except:
#             raise ValueError(str(ele) + ' not found')
#     
#     def __str__(self):
#         self.vals.sort()
#         result = ''
#         for ele in self.vals:
#             result = result + str(ele) + ','
#         return '{' + result[:-1] + '}'
# =============================================================================
        
class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    def intersect(self, other):
        """
        Takes two sets lets say s1 and s2
        Returns: a new intSet of integers that appear in both s1 and s2
        """
        inter = intSet()
        for ele in self.vals:
            if ele in other.vals:
                inter.insert(ele)
        return inter
    
    def __len__(self):
        count = 0
        for ele in self.vals:
            count += 1
        return count