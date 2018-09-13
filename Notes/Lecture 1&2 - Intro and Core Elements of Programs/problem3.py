# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 15:36:17 2017

@author: jaehy

Problem 3
0.0/15.0 points (graded)
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

    Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

    Longest substring in alphabetical order is: abc

"""

s = input('Input a string: ')

# first character is initially the longest substring by default
count_curr = 1
count_long = 0
start = 0
end = 0

# for every character in s
for i in range(len(s) - 1):
    
    if s[i] <= s[i+1]:
        count_curr += 1
        
        if count_curr > count_long:
            count_long = count_curr
            end = i + 1
            start = end + 1 - count_long
            
    else:
        count_curr = 1


print()
print('Longest substring in alphabetical order is: ' + s[start:end+1])
    
    
    
    