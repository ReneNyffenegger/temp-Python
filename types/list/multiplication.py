#  Multiplication of a list with a number creates a list that contains
#  the elements of the muliplied list n times.
#
print(3 * [ ['foo', ['bar', 'baz' ]] ])

a = ['one', 'two' ]
print(a * 2)
#
# ['one', 'two', 'one', 'two']

b = [ a ] * 2
print(b)
#
# [['one', 'two'], ['one', 'two']]

#
#  the two elements in b refer to the same object!
#

b[0][1] = 'TWO'
print(b)
#
# [['one', 'TWO'], ['one', 'TWO']]

