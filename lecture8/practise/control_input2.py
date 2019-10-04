# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 13:30:57 2019

@author: Sangye Tenphel
"""

data = []
file_name = input("Provided a name of a file of data: ")

try:
    fh = open(file_name, 'r')
except IOError:
    print('cannot open', file_name)
else:
    for new in fh:
        if new != '\n':                  # to avoid the carriage returns else will get empty lists of data
            addIt = new[:-1].split(',')  # split everthing on a comma into a list except the last element i.e. a '\n'
            data.append(addIt)
    fh.close()
    
gradesData = []
if data:                                 # As long as I have data
    for student in data:
        try:
            name = student[0:-1]
            grade = int(student[-1])
            gradesData.append([name, [grade]])
        except ValueError:
            gradesData.append([student[:], []])
        