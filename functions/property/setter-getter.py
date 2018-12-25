#!/usr/bin/python3
#
#    Compare with ../../decorators/getter-setter.py
#

class CLS:

     def __init__(self):
         self._p = None

     def GET(self):
         print('GET')
         return self._p

     def SET(self, val):
         print('SET')
         self._p = val

     def DEL(self):
         print('DEL')
         del self._p

     p = property(GET, SET, DEL)
     print('type(p) = ' + str(type(p)))


obj_1 = CLS()

obj_1.p = 'foo'
print(obj_1.p)

del obj_1.p
