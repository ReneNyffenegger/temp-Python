#!/usr/bin/python

def F(arg, opt1 = 'foo', opt2='bar'):
    print('arg = {:s}, opt1 = {:s}, opt2 = {:s}'.format(arg, opt1, opt2))

F('abc')
F('def', opt2='DEF')
F('ghi', 'GHI')
