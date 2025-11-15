#
#  in ~/github/dev/lang/python/temp/statements/import/ , run
#       python -m ZF.db
#
from .__init__ import *
print(f'ZF.db.__main__, in __main__.py, __name__ = {__name__}, calling open_ZF_db')
open_ZF_db()
dbhelper_func('from __main__.py')


