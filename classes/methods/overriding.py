#!/usr/bin/python3

class A:

   def __eq__(self, o):
       print('xxx')
       return False


class B:
    def p(self): # A method is a function that takes a class instance as its first parameter. 
        print('I am a A')


a = A()
b = B()

if a is b:
   print ('a is b')
else:
   print ('a is not b')

b.p()

if a == b:
   print ('a is b')
