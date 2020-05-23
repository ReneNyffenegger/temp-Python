builtin_types = {}

def ensureTypeInDict(t):
    global builtin_types

#   print(f'  ensureTypeInDict, {t.__name__}, {typeName}')

    if not id(t) in builtin_types:

#      print('   missing')

       builtin_types[id(t)] = { 
           'name'    :  t.__name__,
           'aliases' : [],          # special key to store names of aliases (for example: OSError is EnvironmentError is IOError is WindowsError)
           'children': []           # type ids of children
       }
#   else:
#      print('   already here')

#   if not t.__name__ in builtin_types[id(t)]['names']:
#      builtin_type
#      builtin_types[id(t)]['names'].append(typeName)
    

# for builtin_type in [ T for T in [ getattr(__builtins__, B) for B in dir(__builtins__) ]  if issubclass(type(T), type) ]:
# for builtin in [ getattr(__builtins__, B) for B in  dir(__builtins__) ]:

#for builtin_name in dir(__builtins__) + [ 'type' ]  :
for builtin_name in dir(__builtins__):

    builtin_obj = getattr(__builtins__, builtin_name)
 #
 #  Iterate over built-in types, assigning each built-in type to builtin_type
 #

#   builtin_type = type(builtin_obj)
    builtin_type = builtin_obj

    if not issubclass(type(builtin_type), type):
       continue

    if builtin_type is object: 
#      ensureTypeInDict(object)
       continue

    assert len(builtin_type.__bases__) == 1

    type_name = builtin_type.__name__
    base_name = builtin_type.__bases__[0].__name__
    base_type = getattr(__builtins__, base_name)

#   print('builtin_type iteration:', base_name, '->', type_name)

    ensureTypeInDict(builtin_type)
    ensureTypeInDict(base_type   )

#   print(builtin_type)
    if not id(builtin_type) in builtin_types[id(base_type)]['children']:
#      print('appending')
       builtin_types[id(base_type)]['children'].append(id(builtin_type))

#   if builtin_name != builtin_type.__name__ and builtin_name not in builtin_types[id(base_type)]['aliases']:
#      builtin_types[id(builtin_type)]['aliases'].append(builtin_name)


#q #   continue
#q 
#q     if not id(builtin_type) in builtin_types:
#q #      print("ADDING", base_name)
#q        builtin_types[id(type_name)] = { 
#q          'names'   : [ type_name ],          # special key to store names of aliases (for example: OSError is EnvironmentError is IOError is WindowsError)
#q          'children': []
#q        }
#q     else:
#q        builtin_types[id( type_name)].append(type_name)
#q 
#q     builtin_types[base_name]['children'].append({ type_name)
#q #   builtin_types[base_name]['children'].append({ type_name)


def printTypeChildren(typeId, indent = 0):

    print('  ' * indent, end='')
    print(builtin_types[typeId]['name'], end='')

#   if builtin_types[typeId]['aliases']:
#      print(' (', ', '.join(builtin_types[typeId]['aliases'])

    print('')

#   if type_name in builtin_types:
    for child_id in builtin_types[typeId]['children']:
        printTypeChildren(child_id, indent+1)
        

printTypeChildren(id(object))
