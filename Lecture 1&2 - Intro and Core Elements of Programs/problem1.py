# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 15:33:36 2017

@author: jaehy



Problem 1
10.0/10.0 points (graded)
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

    Number of vowels: 5

"""
s = 'wjfoiwjfowjofiwjfhqiog'

count = 0

for char in s:
    if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
        count += 1

print('Number of vowels: ' + str(count))