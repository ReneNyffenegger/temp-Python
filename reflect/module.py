# exec(open('/home/tq84/github/temp/Python/reflect/module.py').read(), {**globals(), "obj": mechanicalsoup})
# exec(open('/home/tq84/github/temp/Python/reflect/module.py').read(), {**globals(), "obj": torch})
# exec(open('/home/tq84/github/temp/Python/reflect/module.py').read(), {**globals(), "obj": torch.Tensor})

# import torch
# obj = mechanicalsoup

import types

for mem in [ _ for _ in sorted(dir(obj), key = lambda m: m.replace('_', '').upper()) if not _.startswith('__') ]:

    member = getattr(obj, mem)
    typ = type(member)
#   print(isinstance(typ, object))

    if   isinstance(member, type(lambda: 0)):
         member = f'{mem}()'
         type_  =  'f'

    elif isinstance(member, type(print)):
         member = f'{mem}()'
         type_  =  'b f/m'

    elif isinstance(member, types.ModuleType):
         member = f'{mem}'
         type_  =  'mod'

    else:
       member = mem
       type_  = str(typ)

    print(f'`{member}` ☰  {type_}' )
