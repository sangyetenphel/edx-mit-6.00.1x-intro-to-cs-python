# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 18:53:25 2019

@author: Sangye Tenphel
"""

class Fraction(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
        
    def __str__(self):
        return str(self.numer) + '/' + str(self.denom)
        
    def getNumer(self):
        return self.numer
    
    def getDenom(self):
        return self.denom
    
    def __add__(self, other):
        numer_sum = (self.getNumer() * other.getDenom()) + (other.getNumer() * self.getDenom())
        denom_sum = self.getDenom() * other.getDenom()
        return Fraction(numer_sum, denom_sum)
        
    def __sub__(self, other):
        numer_diff = (self.getNumer() * other.getDenom()) - (other.getNumer() * self.getDenom()) 
        denom_sum = self.getDenom() * other.getDenom()
        return Fraction(numer_diff, denom_sum)
    
    def convert(self):
        return self.getNumer() / self.getDenom()