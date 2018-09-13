# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 14:53:43 2017

@author: Jae You

desc: bisection search program to find the minimum fixed payment to pay off a debt with compound interest

balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal

"""
def fixedPayment(balance, annualInterestRate):
    originalBalance = balance
    monthlyInterest = annualInterestRate / 12
    
    epsilon = 0.01                                          # accuracy of our function
    lowerBound = balance / 12                               # minimum monthly payment
    upperBound = (balance * (1 + monthlyInterest)**12) / 12 # maxium monthly payment

    while abs(balance) > epsilon:
        balance = originalBalance
        payment =  (lowerBound + upperBound) / 2 

        for month in range(12):
            balance = (balance - payment) + (balance - payment) * (monthlyInterest)

        if balance > epsilon:
            lowerBound = payment
        elif balance < epsilon:
            upperBound = payment
            
    return round(payment, 2)


# test values:
balance = 999999
annualInterestRate = 0.18
print('Lowest payment: {}'.format(fixedPayment(balance, annualInterestRate)))






