#!/usr/bin/python3

#
#  `in` is a shorthand for `__contains__`
#

ary = ['foo', 'bar', 'baz']

if 'bar' in ary:
    print('bar is in ' + str(ary))
else:
    print('bar is not in ' + str(ary))

if ary.__contains__('bar'):
    print('bar is contained in ' + str(ary))
else:
    print('bar is not contained in ' + str(ary))
