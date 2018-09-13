# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 20:08:02 2018

@author: Jae You
"""

try:
    a = int(input("Tell me one number: "))
    b = int(input("Tell me another: "))
    print(a/b)
    print("Okay")
except:
    print("Bug in user input")
print("Outside")