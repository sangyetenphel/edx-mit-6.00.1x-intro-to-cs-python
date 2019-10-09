# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 18:48:28 2019

@author: Sangye Tenphel
"""

class Coordinate(object): 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
# =============================================================================
#     def distance(self, other):
#         x_squared = (self.x - other.x) **2
#         y_squared = (self.y - other.y) **2
#         return (x_squared + y_squared)**0.5
#     
#     def __str__(self): # special method for print
#         return "<" + str(self.x) + ", " + str(self.y) + ">"
#     
#     def __add__(self, other): #special method for self + other
#         sum_x = self.x + other.x
#         sum_y = self.y + other.y
#         return Coordinate(sum_x, sum_y)
# =============================================================================
    
    def getX(self):
    # Getter method for a Coordinate object's x coordinate.
    # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    
    def __eq__(self, other):
        return self.getX() == other.getX() and self.getY() == other.getY()
    
    def __repr__(self):
        try:
            return 'Coordinate(' + str(self.getX()) + ',' + str(self.getY()) + ')'
        except:
            raise ValueError('You are a loser!')
    
c = Coordinate(3, 4)
origin = Coordinate(1, 1)

# =============================================================================
# print(c.x)
# print(origin.x) 
# print(c + origin)
# =============================================================================
