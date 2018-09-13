# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 18:32:52 2017

@author: Jae You


A regular polygon has n number of sides. Each side has length s.

The area of a regular polygon is: 0.25∗n∗s^2 / tan(π/n)
The perimeter of a polygon is: length of the boundary of the polygon
Write a function called polysum that takes 2 arguments, n and s. 
This function should sum the area and square of the perimeter of the regular polygon.
The function returns the sum, rounded to 4 decimal places.


"""
from math import tan, pi

def polysum(n, s):
    """
    n: int; the number of sides of a regular polygon
    s: int; the length of each side
    
    returns: float to nearest 4 decimal ; sum of area and squared perimeter
    """
    
    area = (0.25 * n * s**2) / tan(pi / n)
    
    perimeter = (n * s)
    
    return round(area + perimeter**2, 4)
    