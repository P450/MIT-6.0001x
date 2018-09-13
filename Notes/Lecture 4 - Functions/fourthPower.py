# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 00:34:28 2017

@author: Jae You


Write a Python function, fourthPower, that takes in one number and returns that value raised to the fourth power.

You should use the square procedure that you defined in an earlier exercise
(you don't need to redefine square in this box; when you call square, the grader will use our definition).

This function takes in one number and returns one number.


"""
def square(x):
    '''
    x: int or float.
    '''
    return x**2

def fourthPower(x):
    '''
    x: int or float.
    '''
    return square(square(x))

print('x^4 = ', fourthPower(int(input('x = '))))