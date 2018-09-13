# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 17:01:45 2017

@author: Jae You

Midterm Problem 3


Implement a function called closest_power that meets the specifications below.

For example,

closest_power(3,12) returns 2
closest_power(4,12) returns 2
closest_power(4,1) returns 0
"""
def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    
    if num == 0:
        return 0
    
    else:
        exp = 0
        
        # increment exp until base**exp becomes greater than num
        while base**exp < num:
            exp += 1
        
        # compare the distance of two exponents to num 
        # make sure to return the lower exponent if equal
        if abs(num - base**(exp -1)) <= abs(num - (base**exp)):
            return exp - 1
        else:
            return exp
            
            
print(closest_power(4, 3))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    