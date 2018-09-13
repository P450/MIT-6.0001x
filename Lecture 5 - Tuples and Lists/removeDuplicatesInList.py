# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 20:16:15 2017

@author: Jae You

removing duplicates from a list

"""

"""
THIS DOES NOT WORK:
"""

def remove_dups(L1, L2):
    for e in L1:
        if e in L2:
            L1.remove(e)
            
            
def remove_dups_new(L1,L2):
    L1_copy = L1[:]     # L1_copy = L1 does not clone; it simply creates a copy of the pointer to the same object
    for e in L1_copy:
        if e in L2:
            L1.remove(e)        # changing L1 here doesn't change iterable L1_copy