#!/usr/bin/python3

class ABCD:
      pass

class EFGH:
      pass

abcd = ABCD()
efgh = EFGH()

#
# Every Python class has a built-in class attribute __module__.
# It stores the name of the module in which the class is defined. 
#
print ('abcd.__module__ = {:s}'.format(abcd.__module__)) # __main__
print ('efgh.__module__ = {:s}'.format(efgh.__module__)) # __main__
