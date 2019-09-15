# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 19:32:29 2019

@author: Sangye Tenphel
"""

nameHandle = open('createdFromPython','w')
nameHandle.write('Is it working?')
for i in range(2):
    words = input("Say Something!: ")
    nameHandle.write(words + '\n')
nameHandle.close()
    
nameHandle = open('createdFromPython','r')
for line in nameHandle:
    print(line)
nameHandle.close()