# from use import *

from .dbhelper import *

def open_ZF_db():
    print(f'open_ZF_db, calling dbhelper_func. __name__ = {__name__}')
    dbhelper_func('ZF')
