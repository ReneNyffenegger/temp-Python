class A:

  def m(self):
      print('A.m was called')


class B:

  def m(self):
      print('B.m was called')


class C:

  def M(self):
      self.m()


c = C()

print(C.mro())

C.mro = lambda: (C, A, object)

print(C.mro())

# assert not hasattr(c, 'm')
# assert     hasattr(c, 'M')
# 
# C.__mro__ = A, C
c.M()
