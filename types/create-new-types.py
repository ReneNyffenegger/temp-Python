print(type('text'))
#
#   <class 'str'>

print(type(type))
#
#   <class 'type'>


class CLS:
      pass

print(type(CLS))
#
#  <class 'type'>

inst = CLS()
print(type(inst))
#
#  <class '__main__.CLS'>

xyzClass = type('XYZ', (), {})
print(type(xyzClass))
#
#  <class 'type'>

xyzInstance = xyzClass()
print(type(xyzInstance))
#
#  <class '__main__.XYZ'>
