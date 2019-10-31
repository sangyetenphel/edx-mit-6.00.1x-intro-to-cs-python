# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 22:37:36 2019

@author: Sangye Tenphel
"""

'''
Object-Oriented Programming (OOP) is a programming model focused on
real-life objects, instead of processes that only input and output data
'''

class MITxStaff(object):
    firstName = ""
    lastName = ""

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

class TA(MITxStaff):
    awesomenessLevel = 0

    def __init__(self, firstName, lastName, awesomenessLevel):
        self.awesomenessLevel = awesomenessLevel
        MITxStaff.__init__(self, firstName, lastName)

    def toString(self):
        return "{} {} has an awesomeness level of {}".format(self.firstName, self.lastName, self.awesomenessLevel) # Use of placeholders i.e. {}

Nitish = TA("Nitish", "Mittal", 100)
Jing = TA("Jing", "Ma", 9001)
print(Nitish.toString())
print(Jing.toString())
