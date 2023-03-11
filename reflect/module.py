
#  MOVED to dot-files/pythonrc ( in after-installing-Linux)

#   # exec(open('/home/tq84/github/temp/Python/reflect/module.py').read(), {**globals(), "obj": mechanicalsoup})
#   # exec(open('/home/tq84/github/temp/Python/reflect/module.py').read(), {**globals(), "obj": torch         })
#   # exec(open('/home/tq84/github/temp/Python/reflect/module.py').read(), {**globals(), "obj": torch.Tensor  })
#   # exec(open('/home/tq84/github/temp/Python/reflect/module.py').read(), {**globals(), "obj": g[1]          })
#   # exec(open('/home/tq84/github/temp/Python/reflect/module.py').read(), {**globals(), "obj": pandas        })
#   # exec(open('/home/tq84/github/temp/Python/reflect/module.py').read(), {**globals(), "obj": 
#   
#   # import torch
#   # obj = mechanicalsoup
#   
#   import types
#   import re
#   
#   for mem in [ _ for _ in sorted(dir(obj), key = lambda m: m.replace('_', '').upper()) if not _.startswith('__') ]:
#   
#    try:
#       member = getattr(obj, mem)
#   
#       typ = type(member)
#   #   print(isinstance(typ, object))
#   
#       if   isinstance(member, type(lambda: 0)):
#            member = f'{mem}()'
#            type_  =  'Function'
#   
#       elif isinstance(member, type(print)):
#            member = f'{mem}()'
#            type_  =  'Built-in function'
#   
#       elif isinstance(member, types.ModuleType):
#            member = f'{mem}'
#            type_  =  'Module'
#   
#       elif str(typ) == "<class 'method'>":
#            member = f'{mem}()'
#            type_  =  'Class method'
#   
#       else:
#          member = mem
#          type_  = str(typ)
#          type_  = re.search(r"<class '(\w+)'>", type_).group(1)
#          if    type_ == 'type':
#                n =       f'{obj.__name__}.{mem}'
#                x =  eval(n)
#                type_ = str(x)
#                type_ = re.search(r"<class '(.+)'>", type_).group(1)
#                type_ = f'`{type_}` class'
#   
#   #            type_ = f'A `{str(type_)
#          else:
#                type_  = f'`{type_}` object'
#   
#       print(f'`{member}` ☰ {type_}' )
#   
#    except:
#       print(f'`{mem}` ☰ ?' )
#     
#   #   print(f'`{member}` ☰  {type_} {str(typ)}' )
