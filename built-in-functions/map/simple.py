def f(i):
    return i * 3

l = [4,5,6]
print(type(l)) # <class 'list'>

print(l[1]) # 5

m = map(f, l)

print(type(m)) # <class 'map'>

# print(m[0]) # TypeError: 'map' object is not subscriptable


l = [6,7,8,9]

for i in m:
    print(i)


m_ = map(lambda n: n*3, l)
print(dir(m_))
for i in m_:
    print(i)
