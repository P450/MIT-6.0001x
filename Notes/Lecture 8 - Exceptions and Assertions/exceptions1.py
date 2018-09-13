# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 13:46:49 2018

@author: Jae You
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 12:57:51 2018

@author: Jae You
"""

data = []
file_name = input("Provide a name of a file of data: ")

try:
    fh = open(file_name, 'r')
except IOError:
    print('cannot open', file_name)
else:
    for line in fh:
        if line != '\n':
            addIt = line[:-1].split(',') # remove trailing \n
            data.append(addIt)
finally:
    fh.close() # close file even if fail

gradesData = []
if data:
    for student in data:
        try:
            name = student[0:-1]
            grades = int(student[-1])   # can throw ValueError if last element not a nubmer
            #gradesData.append([student[0:2], [student[2]]])
            gradesData.append([name, [grades]])
        except ValueError:
            gradesData.append([student[:], []])
