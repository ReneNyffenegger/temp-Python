def f():
    pass
print(f)

var = 42
l = lambda: var * 2
print(l)

var = 43
print( l())



for i in range(5):
      print(lambda: i**2)

for i in range(5):
      print( (lambda: i**2)() )

squares = []
for i in range(5):
      squares.append(lambda: i ** 2)

print(squares[0]())




# print (lambda x: x*3, [4,5,6])
