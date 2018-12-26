#!/usr/bin/python3

def TQ84_decorator(func):
 #
 #  This decorator function is called when the decorated
 #  function is defined.
 #
    print(f'TQ84_decorator was called for func {func.__name__}')
    return func

print('Going to define a function')

@TQ84_decorator
def FuncOne():
    print('Within FuncOne')


print('Going to define another function')

@TQ84_decorator
def FuncTwo():
    print('Within FuncOne')

print('Function was defined, going to call it.')

FuncOne()

print('Function was called.')
