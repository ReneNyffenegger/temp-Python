#!/usr/bin/python3


prims_list = [2, 3, 5, 7, 11, 13, 17]

prims_list_i = iter(prims_list)
print(type(prims_list_i)) # <class list_iterator>

print(next(prims_list_i))
print(next(prims_list_i))
print(next(prims_list_i))
print(next(prims_list_i))
print(next(prims_list_i))
print(next(prims_list_i))
print(next(prims_list_i))

class PRIMES:
    def __init__(self):
        print('__init__')
        self.prims=[2, 3, 5, 7, 11, 13, 17]

    def __iter__(self):
        print('__iter__')
        self.cur = -1
        return self

    def __next__(self):
        print('__next__')
        if self.cur + 1 >= len(self.prims):
           raise StopIteration
        self.cur += 1
        return self.prims[self.cur]
        
        

primes = PRIMES()
p_i = iter(primes)
for p_ in p_i:
      print('p_ = ' + str(p_))

primes_again = PRIMES()
for pa in primes_again:
    print(pa)

yet_again = PRIMES()
iter(yet_again)

try:
   while x := next(yet_again): # PEP-572
         print(x)
except StopIteration:
   print('finished')
