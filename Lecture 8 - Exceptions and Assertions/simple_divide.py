# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 19:53:07 2018

@author: Jae You

Week 4 Lecture 8: simple divide

Suppose we rewrite the FancyDivide function to use a helper function.

def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
   return item / denom
    

This code raises a ZeroDivisionError exception for the following call: fancy_divide([0, 2, 4], 0)

Your task is to change the definition of simple_divide so that the call does not raise an exception. When dividing by 0, fancy_divide should return a list with all 0 elements. Any other error cases should still raise exceptions. You should only handle the ZeroDivisionError.


"""

def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
   try:
       item / denom
   except ZeroDivisionError:
       return 0


# answer:
## still takes same arguments
#def simple_divide(item, denom):
#   # start a try-except block
#   try:
#      return item / denom
#   # catch a division by zero and return 0
#   except ZeroDivisionError:
#      return 0