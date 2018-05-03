#!/usr/bin/python

class aClass:
    def __init__(self, data):
        self.data = data

    def printData(self):
        print('data = {:s}'.format(self.data))

#
#  Note: no need to use a 'new' operator to instantiate an
#  instance of a class:
#
anInstance      = aClass('foo')
anotherInstance = aClass('bar')

anInstance     .printData()
anotherInstance.printData()
