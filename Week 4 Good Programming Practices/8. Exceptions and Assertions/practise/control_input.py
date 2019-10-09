# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 12:31:12 2019

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
        addIt = new[:-1].split(',')  # split everthing on a comma into a list except the last element i.e. a '\n'
        data.append(addIt)
    fh.close()