# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:17:17 2017

@author: Jae You


Consider the following sequence of expressions:

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
We want to write some simple procedures that work on dictionaries to return information.

This time, write a procedure, called biggest, which returns the key corresponding to the entry with the largest number of values associated with it.
If there is more than one such entry, return any one of the matching keys.

Example usage:

>>> biggest(animals)
'd'
If there are no values in the dictionary, biggest should return None.


"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    try:
        tuples = ()
        for k,v in aDict.items():
            tuples += ((len(v),k),)
        return max(tuples)[1]
    
        # condensed version:
        #return max((len(v),k) for k,v in aDict.items())[1]
        
        # another version:
        # max(aDict, key = lambda x: len(aDict[x]))
        
    
    except ValueError:
        return None
    
    
    
## solution:    
#def biggest(aDict):
#    result = None
#    biggestValue = 0
#    for key in aDict.keys():
#        if len(aDict[key]) >= biggestValue:
#            result = key
#            biggestValue = len(aDict[key])
#    return result
