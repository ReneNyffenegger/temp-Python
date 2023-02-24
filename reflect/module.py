# exec(open('/home/tq84/github/temp/Python/reflect/module.py').read(), {**globals(), "obj": mechanicalsoup})

# import torch
# obj = mechanicalsoup

for mem in [ _ for _ in sorted(dir(obj), key = lambda m: m.replace('_', '')) if not _.startswith('__') ]:

    member = getattr(obj, mem)
    typ = type(member)
#   print(isinstance(typ, object))

    if isinstance(member, type(lambda: 0)):
       member = f'{mem}()'
       type_  =  ''

    else:
       member = mem
       type_  = str(typ)

    print(f'`{member}` ☰  {type_}' )
