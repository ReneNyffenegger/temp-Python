
print(type(list))

# list.join = lambda X: x.join(self)
# print(dir(list))
# print(type(list.__class__))
# print(dir(list.__class__))

l = ['foo', 'bar', 'baz']

def j(self, x):
    return x.join(self)

l.join = j
#
#  AttributeError: 'list' object has no attribute 'join'

# print(type(l.join))

# print(l.join(' - '))
