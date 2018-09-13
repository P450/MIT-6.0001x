# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 12:30:33 2018

@author: Jae You
"""

def isPal (x):
    assert type(x) == list
    temp = x[:]
    print('before', x, temp)
    temp.reverse()
    print('after', x, temp)
    if temp == x:
        return True
    else:
        return False

def silly(n):
    result = []
    for i in range(n):
        elem = input('Enter element: ')
        result.append(elem)
    if isPal(result):
        print('Yes')
    else:
        print('No')
        