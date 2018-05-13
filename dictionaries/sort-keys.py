#!/usr/bin/python

aDict= {'one'  : 1,
        'two'  : 2,
        'three': 3,
        'four' : 4,
        'five' : 5
       }

for k in sorted(aDict):
    print('{:5s}: {:d}'.format(k, aDict[k]))
