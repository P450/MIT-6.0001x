# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 14:22:26 2017

@author: jaehy
"""

s = 'abcdefghij'

for i in range(len(s)):
    print("index", i, s[i], end='     ')
    print("slice", i, s[i: i+2])

for i, c in enumerate(s):
    print(i, c)

for i in enumerate(s):
    print(s[i: i+5])
