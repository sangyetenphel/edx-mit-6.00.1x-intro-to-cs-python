# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 20:43:44 2019

@author: Sangye Tenphel
"""

def get_ratios(L1, L2):
    '''
    Assumes: L1 and L2 are lists of equal length
    Returns: a list cotaining L1[i]/L2[i]
    '''
    ratios = []
    for i in range(len(L1)):
        try:
            ratios.append(L1[i]/L2[i])
        except ZeroDivisionError:
            ratios.append('NaN') #Nan = Not a number
        except:
            raise ValueError('get_ratios called with bad arg')
    return ratios

