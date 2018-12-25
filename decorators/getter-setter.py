#!/usr/bin/python3
#
#   https://stackoverflow.com/a/18583708/180275
#
#   Compare with ../functions/property/setter-getter.py

class C(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        print('  property x')
        return self._x

    @x.setter
    def x(self, value):
        print('  setter x')
        self._x = value

    @x.deleter
    def x(self):
        print('  deleter x')
        del self._x



c_1  = C()
c_2  = C()

print('Assigning one')
c_1.x = 'one'

print('Assigning two')
c_2.x = 'two'

print('Getting one')
print('  ' + c_1.x)

print('Getting two')
print('  ' + c_2.x)

del c_1.x
print('  ' + c_1.x)
