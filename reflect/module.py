# exec(open('/home/tq84/github/temp/Python/reflect/module.py').read(), {**globals(), "obj": mechanicalsoup})

# import torch
# obj = mechanicalsoup

for member in [ _ for _ in sorted(dir(obj), key = lambda m: m.replace('_', '')) if not _.startswith('__') ]:
    print(member + '\t' + str(type(getattr(obj, member))))
