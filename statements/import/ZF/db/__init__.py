# from use import *

print(f"db.__init__.py, __package__ = {__package__}, __name__ = {__name__}")

if __package__:
  from .dbhelper import *
else:
  from dbhelper import *


def open_ZF_db():
    print(f'open_ZF_db, calling dbhelper_func. __name__ = {__name__}, __package__ = {__package__}')
    dbhelper_func('ZF')

if  __name__ == '__main__':
    print(f"ZF.__init__.py: __name__ == {__main__}")
    pass
#   import sys

   
