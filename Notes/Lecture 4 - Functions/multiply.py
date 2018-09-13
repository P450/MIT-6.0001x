# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 10:40:27 2017

@author: Jae You
"""

def multiply(a, b):
    if b == 1:
        return a
    else:
        return a + multiply(a, b - 1)

a, b = map(int, input('input two integers: ').split() )

print(multiply(a, b))