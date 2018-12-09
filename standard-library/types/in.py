#!/usr/bin/python2
# Does not work in python 3???
import types

d = {}
l = []

if type(d) is types.DictType:
   print('d is types.DictType')

if type(d) in types.StringTypes:
   print('d is types.StringTypes')

if type(l) is types.DictType:
   print('l is types.DictType')

if type(l) in types.StringTypes:
   print('d is types.StringTypes')
