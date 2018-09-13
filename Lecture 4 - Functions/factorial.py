# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 02:53:41 2017

@author: Jae You
"""

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)
    
print(factorial(10))