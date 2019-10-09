# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 22:15:00 2019

@author: Sangye Tenphel
"""

# =============================================================================
# def credit_card_balance(balance, annualInterestRate, monthlyPaymentRate):
#     for i in range(12):
#         min_pay = monthlyPaymentRate * balance
#         unpaid_bal = balance - min_pay
#         interest = (annualInterestRate/12.0) * unpaid_bal
#         balance = unpaid_bal + interest
#     return round(balance, 2)
# 
# balance = 42
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04
# 
# result = credit_card_balance(balance, annualInterestRate, monthlyPaymentRate)
# print("Remaining balance:", result)
# =============================================================================


# Paste your code into this box
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for i in range(12):
    min_pay = monthlyPaymentRate * balance
    unpaid_bal = balance - min_pay
    interest = (annualInterestRate/12.0) * unpaid_bal
    balance = unpaid_bal + interest
    
print("Remaining balance:", round(balance, 2))





