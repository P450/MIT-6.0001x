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
            gradesData.append([student[0:2], [student[2]]])
        except IndexError:
            gradesData.append([student[0:2], []])

            
#data
#Out[56]: 
#[['first', 'last', '100'],
# ['jae', 'you', '90'],
# ['eric', 'grimsom', '80'],
# ['no', 'grad']]

#gradesData
#Out[57]: 
#[[['first', 'last'], ['100']],
# [['jae', 'you'], ['90']],
# [['eric', 'grimsom'], ['80']],
# [['no', 'grad'], []]]
            
#gradesData[3][1]
#Out[63]: []