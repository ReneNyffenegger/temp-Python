
obj = object();

# An object instance has no __dict__ attribute

for d in dir(obj):
    print(d)

#
# Without __dict__ attribute, it's apparently not possible to
# assign a new attribute:
#
# obj.x = 'eggs'
# obj.y = 'why'
# obj.z  = 42

class C(object):
    def __init__(self):
      pass
    # print(type(self))
    # self.x = 'eggs'
    # self.y = 'why'
    # self.z =  42


#
# An instance of a class has a __dict__ attribute
#   (Except if it is created with the __slots__ thingy)
#
c = C()
for d in dir(c):
    print(d)

#
# With the __dict__ attribute, it's possible to create an attribute
# on the instance
#
c.foo_bar_baz = 42

print ('-----------')
print (c.__dict__['foo_bar_baz'])
