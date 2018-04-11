class Foo:
    def f_one(self):
        print('hello')

    def f_two(self):
        pass

for k in Foo.__dict__:
    print('k = {:s}'.format(k))
#
# k = __module__
# k = f_one
# k = f_two
# k = __dict__
# k = __weakref__
# k = __doc__

foo = Foo()


print ('-------------')
for k in foo.__dict__:
    print('k = {:s}'.format(k))

