#!/usr/bin/python3

def tup_3():
    return ('foo', 'bar', 'baz')

one, two, three = tup_3()

print (one  )
print (two  )
print (three)

tup = tup_3()
print (type(tup)) # <class 'tuple'>
for i in tup:
    print(i)

print(tup[0])
print(tup[1])
print(tup[2])

# Following causes
#   ValueError: not enough values to unpack (expected 4, got 3)
# a,b,c,d = tup_3()

# Following causes
#   ValueError: too many values to unpack (expected 2)
# a,b = tup_3()
