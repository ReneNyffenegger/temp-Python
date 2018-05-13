#!/usr/bin/python

#
#  TODO: https://stackoverflow.com/questions/9001509/how-can-i-sort-a-dictionary-by-key
#

aDict= {'one'  : 1,
        'two'  : 2,
        'three': 3,
        'four' : 4,
        'five' : 5
       }

for k in sorted(aDict):
    print('{:5s}: {:d}'.format(k, aDict[k]))
