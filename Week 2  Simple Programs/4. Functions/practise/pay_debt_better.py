# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 10:32:33 2019

@author: Sangye Tenphel
"""
balance = 320000
annualInterestRate = 0.2

balanceCopy = balance
monthly_interest_rate = annualInterestRate / 12.0
low = balance / 12
high = (balance * (1 + monthly_interest_rate)**12) / 12          
epsilon = 0.01

   
while abs(balance) >= epsilon:
    monthlyPay = (high + low) / 2
    balance = balanceCopy
    
    for i in range(12):
        balance = balance - monthlyPay
        balance += balance * monthly_interest_rate
        
        
    if balance > epsilon:
        low = monthlyPay
    elif balance < -epsilon:
        high = monthlyPay
    else:
        break
    
    
print("Lowest Payment:", round(monthlyPay, 2))



