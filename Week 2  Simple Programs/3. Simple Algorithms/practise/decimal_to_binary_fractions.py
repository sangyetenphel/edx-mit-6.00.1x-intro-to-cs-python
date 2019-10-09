# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 16:26:23 2019

@author: Sangye Tenphel
"""

x = float(input("Enter a decimal number between 0 and 1: "))

p = 0
while (x*(2**p))%1 != 0:
    print("Remainder =", (x*(2**p)) - int(x*(2**p))) # represent the working of the while loop
    p += 1
    
num = int(x*(2**p))

result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num // 2
    
for i in range(p - len(result)):
    result = '0' + result
    
result =  result[0:-p] + '.' + result[-p:]
print("The binary representation of the decimal",x,"is",result)