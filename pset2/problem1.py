# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 19:20:17 2017

@author: Jae You

balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal
monthlyPaymentRate - minimum monthly payment rate as a decimal

"""

def remainingBalance(balance, annualInterestRate, monthlyPaymentRate):
    """
    returns remaining balance after interest and paying minimum monthly payment
    """
    monthInterestRate = annualInterestRate / 12.0
    minMonthPay       = monthlyPaymentRate * balance   
    unpaidBalance     = balance - minMonthPay    
    balance           = unpaidBalance + (monthInterestRate * unpaidBalance)
    
    return balance

month = 0

# test values: 
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

# repeat 
while month < 12:
    balance = remainingBalance(balance, annualInterestRate, monthlyPaymentRate)
    month += 1

print(round(balance, 2))




