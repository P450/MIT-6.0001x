# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 17:47:47 2017

@author: jaehy
"""

x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) < epsilon:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
