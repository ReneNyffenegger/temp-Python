#!/usr/bin/python

# Compare with https://github.com/ReneNyffenegger/about-python/blob/master/built-in/functions/open/readline.py

import sys

f = open('read-lines-from-file.py')
l = f.readline()

# Follows an empty line:

# ...

while l:
    sys.stdout.write(l)
    l = f.readline()
