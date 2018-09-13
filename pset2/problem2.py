# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 21:41:09 2017

@author: Jae You

balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal

Annual interest = 0.2 
Equivalent monthly rate = (1+ 0.2/12)^12 -1

3329= R *((1+(monthly rate)^12) -1)/monthly rate  

"""
# test values:
balance = 3926
annualInterestRate = 0.2

def monthlyPayment(balance, annualInterestRate): 
    payment = 10

    while True:
        outstanding = balance
        
        for month in range(12):
            outstanding = (outstanding - payment) + (annualInterestRate / 12.0 * (outstanding - payment))
        if outstanding > 0:
            payment += 10
        else:
            return payment

print('Lowest Payment: {}'.format(monthlyPayment(balance, annualInterestRate)))


#
#monthlyPaymentRate = 0
#init_balance = balance
#monthlyInterestRate = annualInterestRate/12
#
#while balance > 0:
#    for i in range(12):
#        balance = balance - monthlyPaymentRate + ((balance - monthlyPaymentRate) * monthlyInterestRate)
#    if balance > 0:
#        monthlyPaymentRate += 10
#        balance = init_balance
#    elif balance <= 0:
#        break
#print('Lowest Payment:', monthlyPaymentRate)





#solving algebraically to get the exact value
#
#c = capital
#r = rate
#p = payment
#
#outstanding = cr**n - p(r**n-1 + r**n-2 + ... + r**0)
#at n = 12, outstanding = 0. Thus,
#    p = (cr**2)((1-r)/(1-r**2))




















