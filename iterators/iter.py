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

class PRIMS:
    def __init__(self):
        print('__init__')
        self.prims=[2, 3, 5, 7, 11, 13, 17]

    def __iter__(self):
        self.cur = -1
        return self

    def __next__(self):
        if self.cur + 1 >= len(self.prims):
           raise StopIteration
        self.cur += 1
        return self.prims[self.cur]
        
        

prims = PRIMS()
p_i = iter(prims)
for p_ in p_i:
      print('p_ = ' + str(p_))
