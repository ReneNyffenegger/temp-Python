#!/usr/bin/python

import gc

print("\n".join(sorted({attrname for item in gc.get_objects() for attrname in dir(item) if attrname.startswith("__")})))
