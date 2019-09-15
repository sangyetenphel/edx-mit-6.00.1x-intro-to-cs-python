# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 22:51:58 2019

@author: Sangye Tenphel
"""

balance = 3329
annualInterestRate = 0.2
          
balanceCopy = balance
monthlyPay = 10
   
while True:
    for i in range(12):
        min_pay = monthlyPay
        unpaid_bal = balanceCopy - min_pay
        interest = (annualInterestRate/12.0) * unpaid_bal
        balanceCopy = unpaid_bal + interest
        
    if balanceCopy <= 0:
        break
    
    monthlyPay += 10  
    balanceCopy = balance
    
print("Lowest Payment:", monthlyPay)


