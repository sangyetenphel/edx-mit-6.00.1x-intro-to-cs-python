# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:44:19 2019

@author: Sangye Tenphel
"""

def get_stats(heroes_list):
    '''
    heroes_list: A list of first and last name and a list of grades for heroes
    returns: a new heroes list, with name, grades, and an average
    '''
    new_stats = []
    for heroes in heroes_list:
        new_stats.append([heroes[0], heroes[1], avg(heroes[1])])
    return new_stats
        
def avg(points):
    try:
        return sum(points)/len(points)
    except ZeroDivisionError:                       
        print('No test score for some Heroes!')     # flags the error message
        return 0.0                                  # heroes with no grades get zero
        

test_grades = [[['peter', 'parker'], [10.0, 5.0, 85.0]],
 [['bruce', 'wayne'], [10.0, 8.0, 74.0]],
 [['captain', 'america'], [8.0,10.0,96.0]],
 [['deadpool'], []]]