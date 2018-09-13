# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 20:48:35 2017

@author: Jae You

Problem 5

Write a Python function that returns a list of keys in aDict that map to integer values that are unique (i.e. values appear exactly once in aDict).
The list of keys you return should be sorted in increasing order.
(If aDict does not contain any unique values, you should return an empty list.)

This function takes in a dictionary and returns a list.

"""
def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
        
    list_key = []
    list_value = list(aDict.values())
    
    for k,v in aDict.items():
        if list_value.count(v) == 1:
            list_key += [k,]
    
    
    
    
    
    return sorted(list_key)
    