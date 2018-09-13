# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 16:00:23 2018

@author: Jae You
"""

def get_stats(class_list):
    new_stats = []
    for elt in class_list:
        new_stats.append([elt[0], elt[1], average(elt[1])])
    return new_stats

#def avg(grades):
#    return sum(grades)/len(grades)


def average(grades):
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print('no grades data')
        return 0.0


test_grades = [[['peter', 'parker'], [10.0, 5.0, 85.0]],
                [['bruce', 'wayne'], [10.0, 8.0, 74.0]],
                [['captain', 'america'], []] ]

#In[16]: test_grades
#Out[16]: 
#[[['peter', 'parker'], [10.0, 5.0, 85.0]],
# [['bruce', 'wayne'], [10.0, 8.0, 74.0]],
# [['captain', 'america'], []]]

#In[17]: get_stats(test_grades)      without return 0.0
#no grades data
#Out[17]: 
#[[['peter', 'parker'], [10.0, 5.0, 85.0], 33.333333333333336],
# [['bruce', 'wayne'], [10.0, 8.0, 74.0], 30.666666666666668],
# [['captain', 'america'], [], None]]


#############
#In [1]: s = []
#In [2]: b = []
#In [3]: b.append(average(s))
#no grades data
#
#In [4]: b
#[None]

# with return 0.0 #:

#In [18]: get_stats(test_grades)
#no grades data
#Out[18]: 
#[[['peter', 'parker'], [10.0, 5.0, 85.0], 33.333333333333336],
# [['bruce', 'wayne'], [10.0, 8.0, 74.0], 30.666666666666668],
# [['captain', 'america'], [], 0.0]]








