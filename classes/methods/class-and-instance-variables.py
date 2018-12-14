#!/usr/bin/python3

class aClass:

    instanceCounter = 0

    def __init__(self, data):
        self.data = data
        aClass.instanceCounter += 1

    def printData(self):
        print('data = {:s}, instanceCounter = {:d}'.format(self.data, aClass.instanceCounter))

#
#  Note: no need to use a 'new' operator to instantiate an
#  instance of a class:
#
anInstance      = aClass('foo')
anInstance     .printData()

anotherInstance = aClass('bar')
anotherInstance.printData()

anInstance     .printData()
