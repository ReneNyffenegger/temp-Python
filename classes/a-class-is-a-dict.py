#!/usr/bin/python3

class C:
    def f_one(self):
        print('hello')

    def f_two(self):
        pass

for k in C.__dict__:
    print('k = {:s}'.format(k))
#
# k = __module__
# k = f_one
# k = f_two
# k = __dict__
# k = __weakref__
# k = __doc__

obj_1 = C()
obj_2 = C()

obj_2.x = 'eggs'
obj_2.y = 'why'


print ('-------------')
for k in obj_1.__dict__:
    print('k = {:s}'.format(k))

print ('-------------')
for k in obj_2.__dict__:
    print('k = {:s}'.format(k))
