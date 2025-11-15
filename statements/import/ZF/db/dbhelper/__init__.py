import sys

def dbhelper_func(a):
#   pass
    print(f'dbhelper_func, a = {a}, __name__ = {__name__}, __package__ = {__package__} ({type(__package__)}) ({type(sys.modules[__name__])})')

