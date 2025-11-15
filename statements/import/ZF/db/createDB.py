#!/usr/bin/env python3


# Use this function from a parent directory like so
#    python3 -m ZF.db.createDB
#
# ... but ... thanks to the if __package__
#     it can also be executed as script!

# import importlib

# None of the following wirk
#
# __import__('db', globals=globals(), level = 0)
# importlib.import_module('__init__.py')

if __package__:
   from .__init__ import *
else:
   from __init__ import *



print(f"createDB.py __package__ = {__package__}, __name__ = {__name__}, but must open the DB first")
open_ZF_db()
print("createDB.py: now actually using dbhelper")
dbhelper_func('dbhelper functionality called from createDB.py')
