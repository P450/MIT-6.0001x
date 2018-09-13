# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 11:14:03 2018

@author: Jae You
"""

def avg(grades):
    assert type(grades) == list
    
    assert not len(grades) == 0, 'no grades data'
    return sum(grades)/len(grades)