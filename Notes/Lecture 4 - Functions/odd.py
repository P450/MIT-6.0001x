# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 01:09:43 2017

@author: Jae You

Write a Python function, odd, that takes in one number and
returns True when the number is odd and False otherwise.

You should use the % (mod) operator, not if.

This function takes in one number and returns a boolean.


"""

def odd(x):
    """
    x: int
    returns: True if x is odd, False otherwise
    """
    return (x % 2 == 1)
    