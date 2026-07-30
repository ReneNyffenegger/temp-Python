-----------------------------
-----------------------------

python3 -m A

#  A.__init__.py, __name__ = A, __file__ = /home/rene/github/dev/lang/python/temp/modules-packages/A/__init__.py, __package__ = A
#  A.__main__.py, __name__ = __main__, __file__ = /home/rene/github/dev/lang/python/temp/modules-packages/A/__main__.py

echo -----------------------------

#  A.__init__.py, __name__ = A, __file__ = /home/rene/github/dev/lang/python/temp/modules-packages/A/__init__.py, __package__ = A
#  A.scr, __name__ = __main__, __file__ = /home/rene/github/dev/lang/python/temp/modules-packages/A/scr.py, __packkge__ = A

python3 -m A.scr

echo -----------------------------

python3 -m A.B

#  A.__init__.py, __name__ = A, __file__ = /home/rene/github/dev/lang/python/temp/modules-packages/A/__init__.py, __package__ = A
#  B.__init__.py, __name__ = A.B, __file__ = /home/rene/github/dev/lang/python/temp/modules-packages/A/B/__init__.py, __package__ = A.B
#  B.__main__.py, __name__ = __main__, __file__ = /home/rene/github/dev/lang/python/temp/modules-packages/A/B/__main__.py
