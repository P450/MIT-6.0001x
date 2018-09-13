# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 15:35:11 2017

@author: jaehy

Problem 2
10.0/10.0 points (graded)
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2

"""
s = 'azcbobobegghakl'

count = 0

for i in range(len(s)):
    if s[i:i+3] == 'bob':        #recall [0:3] is from 0 to 3 exclusive (i.e. 0, 1, 2)
        count += 1

print('Number of times bob occurs is: ' + str(count))