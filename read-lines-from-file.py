#!/bin/python

import sys

f = open('read-lines-from-file.py')
l = f.readline()

# Follows an empty line:

# ...

while l:
    sys.stdout.write(l)
    l = f.readline()
