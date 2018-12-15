#!/usr/bin/python3
#
# https://stackoverflow.com/a/279586/180275
#

def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate

@static_vars(counter=0)
def foo():
    foo.counter += 1
    print("Counter is {:d}".format(foo.counter))

foo()
foo()
foo()
foo()
