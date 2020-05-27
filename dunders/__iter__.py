class CLS:

  def __init__(self):
      self.i = 3

  def __iter__(self):
      print('__iter__')
      return self
      

  def __next__(self):

      if self.i == 1:
         print(f'__next__, raise StopIteration')
         raise StopIteration

      self.i -= 1
      print(f'__next__, returning {self.i}')
      return self.i
      

obj = CLS()

i = iter(obj)

try:

    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))

except StopIteration:
    print('Caught StopIteration')

for num in CLS():
    print(f'num: {num}')
