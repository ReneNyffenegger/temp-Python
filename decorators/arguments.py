#!/usr/bin/python3

def TQ84_decoratorReturnDecorator(argMultiplier):

    print('TQ84_decoratorReturnDecorator was called')

    def TQ84_decoratorMultArg(func):
        print(f'TQ84_decoratorMultArg was called, func.__name__ = {func.__name__}')

        def wrapper(arg):
            return func(arg * argMultiplier)

        return wrapper

    print('TQ84_decoratorReturnDecorator: return TQ84_decoratorMultArg')
    return TQ84_decoratorMultArg


#
#  First, TQ84_decoratorReturnDecorator(3) is called
#  which returns a decorator, that takes a func as argument when
#  then, finally, returns the »new« function.
#
@TQ84_decoratorReturnDecorator(3)
def F1(arg):
    print(f'F1, arg = {arg}')

F1(4)
