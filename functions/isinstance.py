#!/usr/bin/python3
class Base       : pass
class Deriv(Base): pass
class X          : pass


b = Base ()
d = Deriv()
x = X    ()

if isinstance(b   , Base): print('b is an instance of Base')
if isinstance(d   , Base): print('d is an instance of Base')
if isinstance(x   , Base): print('x is an instance of Base')
if isinstance(Base, type): print('Base is an instance of type')
