#!/usr/bin/python3


def F(text):
    if not hasattr(F, 'static_var'):
       F.static_var = ''

    print('F was called, last text was ' + F.static_var + ', current text is ' + text)
    F.static_var = text
       
F('foo')
F('bar')
F('baz')
