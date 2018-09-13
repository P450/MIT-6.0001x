# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 17:23:23 2017

@author: Jae You


Output:
    
inside func_a
None           <-- func_a() has no return so it returns None
inside func_b
7
inside func_c
inside func_a
None


"""

def func_a():
    print('inside func_a')
def func_b(y):
    print('inside func_b')
    return y
def func_c(z):
    print('inside func_c')
    return z()

print(func_a())
print(5 + func_b(2))
print(func_c(func_a))