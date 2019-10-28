# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 13:16:36 2019

@author: Sangye Tenphel
"""

import matplotlib.pyplot as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)
 
plt.figure('Lin')
plt.plot(mySamples, myLinear)
plt.figure('Quad')
plt.plot(mySamples, myQuadratic)
plt.figure("Expo")
plt.plot(mySamples, myExponential)