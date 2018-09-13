# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 12:09:43 2017

@author: Jae You

One method of generating guesses:
    - exhaustive enumeration
    - bisection search
    - newton-raphson (for root finding)

"""

epsilon = 0.01
y = 124.0
guess = y/2.0
numGuesses = 0

while abs(guess**2 - y) >= epsilon:
    numGuesses += 1
    guess = guess - ( ((guess**2)-y) / (2 * guess) )

print('numGuesses = ' + str(numGuesses))
print('Square root of ' + str(y) + ' is about ' + str(guess))