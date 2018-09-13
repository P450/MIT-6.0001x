# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 11:48:08 2017

@author: Jae You

Write an iterative function iterPower(base, exp) that calculates the exponential base^exp by simply using successive multiplication.
For example, iterPower(base, exp) should compute baseexp by multiplying base times itself exp times. Write such a function below.

This function should take in two values - base can be a float or an integer; exp will be an integer ≥ 0.
It should return one numerical value. Your code must be iterative - use of the ** operator is not allowed.


"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    power = 1
    
    if (exp == 0):
        return power
    else:
        for i in range(1, exp + 1):
            power *= base
        return power

print(iterPower(2, 3))




#solution
#def iterPower(base, exp):
#    '''
#    base: int or float.
#    exp: int >= 0
#
#    returns: int or float, base^exp
#    '''
#    result = 1
#    while exp > 0:
#        result *=base
#        exp -= 1
#    return result
