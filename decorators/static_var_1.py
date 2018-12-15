#!/usr/bin/python3
#
# https://stackoverflow.com/a/279586/180275
#

def static_var(varname, value):
    def decorate(func):
        setattr(func, varname, value)
        return func
    return decorate

@static_var("counter", 0)
def foo():
    foo.counter += 1
    print("Counter is {:d}".format(foo.counter))

foo()
foo()
foo()
foo()
