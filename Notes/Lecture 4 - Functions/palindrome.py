# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 23:22:06 2017

@author: Jae You
"""

def isPalindrome(s):
    ''' check if a given string is a palindrome'''
    # return only characters from a string
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans
    
    # check if first and last characters are equal
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
        
    return isPal(toChars(s))