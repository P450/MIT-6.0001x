# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 21:58:21 2017

@author: Jae You

The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. For example,

gcd(2, 12) = 2

gcd(6, 12) = 6

gcd(9, 12) = 3

gcd(17, 12) = 1

A clever mathematical trick (due to Euclid) makes it easy to find greatest common divisors. Suppose that a and b are two positive integers:

    If b = 0, then the answer is a
    
    Otherwise, gcd(a, b) is the same as gcd(b, a % b)

Write a function gcdRecur(a, b) that implements this idea recursively. This function takes in two positive integers and returns one integer.

"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    small = min(a, b)
    large = max(a, b)
    
    if small == 0:
        return large
    else:
        remainder = large % small
        return gcdRecur(remainder, small)

# test value
# print(gcdRecur(1071, 462))


# solution:
#def gcdRecur(a, b):
#    '''
#    a, b: positive integers
#    
#    returns: a positive integer, the greatest common divisor of a & b.
#    '''
#    # Base case is when b = 0
#    if b == 0:
#        return a
#
#    # Recursive case
#    return gcdRecur(b, a % b)
