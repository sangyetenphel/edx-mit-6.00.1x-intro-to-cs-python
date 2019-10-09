# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 13:39:03 2019

@author: Sangye Tenphel
"""

class Weird(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return X
    def getY(self):
        return y

class Wild(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return self.x 
    def getY(self):
        return self.y

X = 7
Y = 8

w1 = Weird(X, Y)
print(w1.getX())