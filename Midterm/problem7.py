# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 22:00:40 2017

@author: Jae You

Write a function called general_poly, that meets the specifications below.
For example, general_poly([1, 2, 3, 4])(10) should evaluate to 1234 because 1∗10^3 + 2 ∗ 10^2 + 3∗10^1 + 4∗10^0.
"""
def general_poly (L):
    """
    L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0
    """
    def inner_poly(x):
        result = 0
        length = len(L)
    
        for i in range(length):
            result += L[i] * x**(length - i - 1)
        return result
            
    return inner_poly
    