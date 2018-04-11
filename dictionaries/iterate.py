
d = {1: 'one',
     2: 'two',
     3: 'three'}

for num in d:
    print('{:d} = {:s}'.format(num, d[num]))

for num in d.keys(): # Same as above(?), but explicitely uses keys()
    print('{:d} = {:s}'.format(num, d[num]))

for num, txt in d.items():
    print('{:d} = {:s}'.format(num, txt))
