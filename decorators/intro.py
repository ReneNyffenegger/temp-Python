#!/usr/bin/python3


def tq84_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before call of " + func.__name__ + ' (' + (', '.join(str(i) for i in args) ) + ')')
        result = func(*args, **kwargs)
        print("After call of " + func.__name__)
        return result
    return wrapper

@tq84_decorator
def add(a, b):
    return a + b

add(1, 3)
