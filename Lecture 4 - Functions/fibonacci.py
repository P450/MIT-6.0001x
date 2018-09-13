# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 23:00:43 2017

@author: Jae You


"""

def fib(x):
    """
    assumes x an int >= 0
    returns Finobacci of x
    """
    if x == 0 or x ==1:
       return 1
    else:
       return fib(x-1) + fib(x-2)