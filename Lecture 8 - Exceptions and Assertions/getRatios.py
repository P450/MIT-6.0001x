# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 14:27:53 2018

@author: Jae You
"""

def get_ratios(L1, L2):
    """ Assumes: L1 and L2 are lists of equal length of numbers
        Retruns: a list containing L1[i]/L2[i] """ 
    ratios = []
    for index in range(len (L1)):
        try:
            ratios.append(L1[index]/float(L2[index]))
        except ZeroDivisionError:
            ratios.append(float('NaN')) # NaN = Not a Number
        except:
            raise ValueError ('get_ratios called with bad arg')
    return ratios


#get_ratios([1,2],[2,1])
#Out[13]: [0.5, 2.0]

#get_ratios([1,2],[2,0])
#Out[14]: [0.5, nan]
    
#get_ratios([1,2],[2])
#Traceback (most recent call last):
#
#  File "<ipython-input-12-5d0f25474095>", line 1, in <module>
#    get_ratios([1,2],[2])
#
#  File "C:/Users/jaehy/Documents/MOOC/MIT 6.00.1x/Lecture 8/getRatios.py", line 18, in get_ratios
#    raise ValueError ('get_ratios called with bad arg')
#
#ValueError: get_ratios called with bad arg