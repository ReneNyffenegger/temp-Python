#!/usr/bin/python3

# https://www.bogotobogo.com/python/python_function_with_generator_send_method_yield_keyword_iterator_next.php

def f():
    print('f was called')
    while True:
        val = yield
        print('val = {:f}'.format(val));
        yield val*10

g = f()
print(type(g))

print('calling g.__next__')
g.__next__()
print('calling g.send')
print(g.send(1))

print('calling g.__next__')
g.__next__()
print('calling g.send')
print(g.send(10))

print('calling g.__next__')
g.__next__()
print('calling g.send')
print(g.send(0.5))
